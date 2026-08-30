from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from user_registration import (
    DuplicateUserError,
    InvalidUserTransitionError,
    User,
    UserNotFoundError,
    UserRegistry,
    UserStatus,
    normalize_email,
    normalize_full_name,
    normalize_username,
)


def test_full_name_normalizes_unicode_and_whitespace() -> None:
    assert normalize_full_name("  Maya\t  Chen  ") == "Maya Chen"
    assert normalize_full_name("Ａｌｅｘ") == "Alex"


@pytest.mark.parametrize("value", ["", "   "])
def test_full_name_rejects_blank_text(value: str) -> None:
    with pytest.raises(ValueError, match="blank"):
        normalize_full_name(value)


def test_username_is_canonical_and_case_insensitive() -> None:
    assert normalize_username("  Maya.Chen  ") == "maya.chen"
    assert normalize_username("ＡＢＣ") == "abc"


@pytest.mark.parametrize(
    "value",
    ["ab", ".maya", "maya chen", "maya@chen", "ábc"],
)
def test_username_rejects_values_outside_project_contract(value: str) -> None:
    with pytest.raises(ValueError, match="username must be"):
        normalize_username(value)


def test_email_is_canonicalized_and_idna_domain_is_supported() -> None:
    assert normalize_email("  MAYA@Example.COM ") == "maya@example.com"
    assert normalize_email("user@bücher.example") == "user@xn--bcher-kva.example"


@pytest.mark.parametrize(
    "value",
    [
        "missing-at.example.com",
        "two@@example.com",
        "@example.com",
        "user@",
        "first..last@example.com",
        ".first@example.com",
        "last.@example.com",
        "user@example",
        "user@-example.com",
        "user@example-.com",
        "user name@example.com",
    ],
)
def test_email_rejects_invalid_project_formats(value: str) -> None:
    with pytest.raises(ValueError):
        normalize_email(value)


def test_user_constructor_normalizes_and_is_immutable() -> None:
    user = User(1, "  Maya   Chen ", "Maya.Chen", "MAYA@example.com")

    assert user.full_name == "Maya Chen"
    assert user.username == "maya.chen"
    assert user.email == "maya@example.com"
    assert user.status is UserStatus.ACTIVE

    with pytest.raises(FrozenInstanceError):
        user.email = "other@example.com"  # type: ignore[misc]


@pytest.mark.parametrize("user_id", [0, -1])
def test_user_rejects_non_positive_ids(user_id: int) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        User(user_id, "Maya Chen", "maya", "maya@example.com")


def test_user_rejects_boolean_id() -> None:
    with pytest.raises(TypeError, match="integer"):
        User(True, "Maya Chen", "maya", "maya@example.com")


def test_register_assigns_sequential_ids_after_success() -> None:
    registry = UserRegistry()

    first = registry.register("Maya Chen", "maya", "maya@example.com")
    second = registry.register("Noah Rivera", "noah", "noah@example.org")

    assert first.user_id == 1
    assert second.user_id == 2
    assert registry.users == (first, second)


def test_failed_registration_does_not_consume_an_id() -> None:
    registry = UserRegistry()
    registry.register("Maya Chen", "maya", "maya@example.com")

    with pytest.raises(DuplicateUserError):
        registry.register("Other Maya", "MAYA", "other@example.com")

    second = registry.register("Noah Rivera", "noah", "noah@example.org")
    assert second.user_id == 2


def test_duplicate_username_is_case_insensitive_and_does_not_mutate() -> None:
    registry = UserRegistry()
    original = registry.register("Maya Chen", "maya.chen", "maya@example.com")

    with pytest.raises(DuplicateUserError, match="username"):
        registry.register("Other User", "MAYA.CHEN", "other@example.com")

    assert registry.users == (original,)


def test_duplicate_email_is_case_insensitive_and_does_not_mutate() -> None:
    registry = UserRegistry()
    original = registry.register("Maya Chen", "maya", "maya@example.com")

    with pytest.raises(DuplicateUserError, match="email"):
        registry.register("Other User", "other", "MAYA@EXAMPLE.COM")

    assert registry.users == (original,)


def test_seeded_registry_validates_duplicates_before_adding_conflict() -> None:
    first = User(10, "Maya Chen", "maya", "maya@example.com")
    duplicate = User(20, "Other", "MAYA", "other@example.com")

    with pytest.raises(DuplicateUserError, match="username"):
        UserRegistry((first, duplicate))


def test_seeded_registry_continues_after_highest_id() -> None:
    registry = UserRegistry(
        (
            User(8, "Maya Chen", "maya", "maya@example.com"),
            User(3, "Noah Rivera", "noah", "noah@example.org"),
        )
    )

    created = registry.register("Lina Costa", "lina", "lina@example.net")
    assert created.user_id == 9


def test_lookup_uses_canonical_username_and_email() -> None:
    registry = UserRegistry()
    user = registry.register("Maya Chen", "Maya.Chen", "MAYA@example.com")

    assert registry.get_by_id(user.user_id) is user
    assert registry.get_by_username("MAYA.CHEN") is user
    assert registry.get_by_email("maya@EXAMPLE.COM") is user


@pytest.mark.parametrize(
    ("method_name", "value"),
    [("get_by_id", 999), ("get_by_username", "missing"), ("get_by_email", "none@example.com")],
)
def test_lookup_raises_clear_not_found_errors(method_name: str, value: object) -> None:
    registry = UserRegistry()
    method = getattr(registry, method_name)

    with pytest.raises(UserNotFoundError):
        method(value)


def test_search_matches_name_username_and_email_in_insertion_order() -> None:
    registry = UserRegistry()
    maya = registry.register("Maya Chen", "maya.design", "maya@example.com")
    noah = registry.register("Noah Rivera", "noah", "design@example.org")
    registry.register("Lina Costa", "lina", "lina@example.net")

    assert registry.search("DESIGN") == (maya, noah)
    assert registry.search("maya") == (maya,)


def test_search_can_filter_by_status() -> None:
    registry = UserRegistry()
    first = registry.register("Maya Chen", "maya", "maya@example.com")
    second = registry.register("Noah Rivera", "noah", "noah@example.com")
    registry.suspend(second.user_id)

    assert registry.search("example", status=UserStatus.ACTIVE) == (first,)
    assert registry.search("example", status=UserStatus.SUSPENDED) == (registry.get_by_id(2),)


def test_search_rejects_blank_query() -> None:
    with pytest.raises(ValueError, match="blank"):
        UserRegistry().search("  ")


def test_change_username_updates_indexes_atomically() -> None:
    registry = UserRegistry()
    user = registry.register("Maya Chen", "maya", "maya@example.com")

    updated = registry.change_username(user.user_id, "Maya.New")

    assert updated.username == "maya.new"
    assert registry.get_by_username("MAYA.NEW") == updated
    with pytest.raises(UserNotFoundError):
        registry.get_by_username("maya")


def test_change_username_rejects_duplicate_without_losing_old_index() -> None:
    registry = UserRegistry()
    first = registry.register("Maya Chen", "maya", "maya@example.com")
    registry.register("Noah Rivera", "noah", "noah@example.org")

    with pytest.raises(DuplicateUserError, match="username"):
        registry.change_username(first.user_id, "NOAH")

    assert registry.get_by_username("maya") == first


def test_change_email_updates_indexes_atomically() -> None:
    registry = UserRegistry()
    user = registry.register("Maya Chen", "maya", "maya@example.com")

    updated = registry.change_email(user.user_id, "MAYA.NEW@Example.com")

    assert updated.email == "maya.new@example.com"
    assert registry.get_by_email("MAYA.NEW@example.com") == updated
    with pytest.raises(UserNotFoundError):
        registry.get_by_email("maya@example.com")


def test_change_email_rejects_duplicate_without_losing_old_index() -> None:
    registry = UserRegistry()
    first = registry.register("Maya Chen", "maya", "maya@example.com")
    registry.register("Noah Rivera", "noah", "noah@example.org")

    with pytest.raises(DuplicateUserError, match="email"):
        registry.change_email(first.user_id, "NOAH@EXAMPLE.ORG")

    assert registry.get_by_email("maya@example.com") == first


def test_change_full_name_normalizes_without_changing_identity_indexes() -> None:
    registry = UserRegistry()
    user = registry.register("Maya Chen", "maya", "maya@example.com")

    updated = registry.change_full_name(user.user_id, "  Maya   L. Chen ")

    assert updated.full_name == "Maya L. Chen"
    assert registry.get_by_username("maya") == updated
    assert registry.get_by_email("maya@example.com") == updated


def test_status_lifecycle_supports_suspend_reactivate_and_deactivate() -> None:
    registry = UserRegistry()
    user = registry.register("Maya Chen", "maya", "maya@example.com")

    suspended = registry.suspend(user.user_id)
    assert suspended.status is UserStatus.SUSPENDED

    active = registry.reactivate(user.user_id)
    assert active.status is UserStatus.ACTIVE

    deactivated = registry.deactivate(user.user_id)
    assert deactivated.status is UserStatus.DEACTIVATED


def test_deactivated_user_is_terminal() -> None:
    registry = UserRegistry()
    user = registry.register("Maya Chen", "maya", "maya@example.com")
    registry.deactivate(user.user_id)

    with pytest.raises(InvalidUserTransitionError):
        registry.reactivate(user.user_id)
    with pytest.raises(InvalidUserTransitionError):
        registry.suspend(user.user_id)
    with pytest.raises(InvalidUserTransitionError):
        registry.deactivate(user.user_id)


def test_list_by_status_returns_only_matching_users() -> None:
    registry = UserRegistry()
    first = registry.register("Maya Chen", "maya", "maya@example.com")
    second = registry.register("Noah Rivera", "noah", "noah@example.org")
    registry.suspend(second.user_id)

    assert registry.list_by_status(UserStatus.ACTIVE) == (first,)
    assert registry.list_by_status(UserStatus.SUSPENDED) == (registry.get_by_id(2),)
    assert registry.list_by_status(UserStatus.DEACTIVATED) == ()
