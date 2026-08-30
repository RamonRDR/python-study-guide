from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, replace
from enum import Enum
from typing import Iterable

USERNAME_PATTERN = re.compile(r"[a-z0-9][a-z0-9._-]{2,29}\Z")
EMAIL_LOCAL_PATTERN = re.compile(r"[a-z0-9.!#$%&'*+/=?^_`{|}~-]+\Z")
DOMAIN_LABEL_PATTERN = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\Z")
MAX_NAME_LENGTH = 80
MAX_EMAIL_LENGTH = 254
MAX_EMAIL_LOCAL_LENGTH = 64
MAX_EMAIL_DOMAIN_LENGTH = 253


class DuplicateUserError(ValueError):
    """Raised when a canonical username or email is already registered."""


class UserNotFoundError(LookupError):
    """Raised when a registry lookup cannot find a user."""


class InvalidUserTransitionError(ValueError):
    """Raised when a requested account-state transition is not allowed."""


class UserStatus(str, Enum):
    """Lifecycle states supported by the educational registry."""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    DEACTIVATED = "deactivated"


def _normalize_unicode(value: str, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be text")
    return unicodedata.normalize("NFKC", value)


def normalize_full_name(value: str) -> str:
    """Return one readable name with normalized Unicode and whitespace."""
    normalized = _normalize_unicode(value, "full_name")
    normalized = " ".join(normalized.split())
    if not normalized:
        raise ValueError("full_name cannot be blank")
    if len(normalized) > MAX_NAME_LENGTH:
        raise ValueError(f"full_name must be at most {MAX_NAME_LENGTH} characters")
    return normalized


def normalize_username(value: str) -> str:
    """Return the canonical, case-insensitive username used by the registry."""
    normalized = _normalize_unicode(value, "username").strip().casefold()
    if not USERNAME_PATTERN.fullmatch(normalized):
        raise ValueError(
            "username must be 3 to 30 ASCII characters, start with a letter or digit, "
            "and use only letters, digits, '.', '_' or '-'"
        )
    return normalized


def _normalize_domain(value: str) -> str:
    if value.startswith(".") or value.endswith(".") or ".." in value:
        raise ValueError("email domain must use valid dot-separated labels")

    try:
        ascii_domain = value.encode("idna").decode("ascii").casefold()
    except UnicodeError as exc:
        raise ValueError("email domain is not valid") from exc

    if len(ascii_domain) > MAX_EMAIL_DOMAIN_LENGTH:
        raise ValueError(
            f"email domain must be at most {MAX_EMAIL_DOMAIN_LENGTH} characters"
        )

    labels = ascii_domain.split(".")
    if len(labels) < 2 or any(not DOMAIN_LABEL_PATTERN.fullmatch(label) for label in labels):
        raise ValueError("email domain must use valid dot-separated labels")
    return ascii_domain


def normalize_email(value: str) -> str:
    """Return the canonical email identifier used by this project."""
    normalized = _normalize_unicode(value, "email").strip().casefold()
    if any(character.isspace() for character in normalized):
        raise ValueError("email cannot contain whitespace")
    if normalized.count("@") != 1:
        raise ValueError("email must contain exactly one '@'")

    local_part, domain = normalized.split("@", 1)
    if not local_part or not domain:
        raise ValueError("email must contain a local part and a domain")
    if len(local_part) > MAX_EMAIL_LOCAL_LENGTH:
        raise ValueError(
            f"email local part must be at most {MAX_EMAIL_LOCAL_LENGTH} characters"
        )
    if (
        local_part.startswith(".")
        or local_part.endswith(".")
        or ".." in local_part
        or not EMAIL_LOCAL_PATTERN.fullmatch(local_part)
    ):
        raise ValueError("email local part is not valid for this project")

    ascii_domain = _normalize_domain(domain)
    canonical = f"{local_part}@{ascii_domain}"
    if len(canonical) > MAX_EMAIL_LENGTH:
        raise ValueError(f"email must be at most {MAX_EMAIL_LENGTH} characters")
    return canonical


def _validate_user_id(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("user_id must be an integer")
    if value <= 0:
        raise ValueError("user_id must be greater than zero")
    return value


@dataclass(frozen=True, slots=True)
class User:
    """Immutable, normalized user snapshot managed by a UserRegistry."""

    user_id: int
    full_name: str
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE

    def __post_init__(self) -> None:
        object.__setattr__(self, "user_id", _validate_user_id(self.user_id))
        object.__setattr__(self, "full_name", normalize_full_name(self.full_name))
        object.__setattr__(self, "username", normalize_username(self.username))
        object.__setattr__(self, "email", normalize_email(self.email))
        if not isinstance(self.status, UserStatus):
            raise TypeError("status must be a UserStatus")


class UserRegistry:
    """Register, index, update, search, and transition fictional users in memory."""

    def __init__(self, users: Iterable[User] = ()) -> None:
        self._users_by_id: dict[int, User] = {}
        self._id_by_username: dict[str, int] = {}
        self._id_by_email: dict[str, int] = {}
        self._next_user_id = 1

        for user in users:
            self._add_existing(user)

        if self._users_by_id:
            self._next_user_id = max(self._users_by_id) + 1

    @property
    def users(self) -> tuple[User, ...]:
        return tuple(self._users_by_id.values())

    def _ensure_identity_available(
        self,
        username: str,
        email: str,
        *,
        excluding_user_id: int | None = None,
    ) -> None:
        username_owner = self._id_by_username.get(username)
        if username_owner is not None and username_owner != excluding_user_id:
            raise DuplicateUserError(f"username '{username}' is already registered")

        email_owner = self._id_by_email.get(email)
        if email_owner is not None and email_owner != excluding_user_id:
            raise DuplicateUserError(f"email '{email}' is already registered")

    def _add_existing(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError("users must contain User values")
        if user.user_id in self._users_by_id:
            raise DuplicateUserError(f"user_id {user.user_id} is already registered")

        self._ensure_identity_available(user.username, user.email)
        self._users_by_id[user.user_id] = user
        self._id_by_username[user.username] = user.user_id
        self._id_by_email[user.email] = user.user_id

    def register(self, full_name: str, username: str, email: str) -> User:
        """Validate and register one active user without consuming IDs on failure."""
        candidate = User(
            user_id=self._next_user_id,
            full_name=full_name,
            username=username,
            email=email,
        )
        self._ensure_identity_available(candidate.username, candidate.email)

        self._users_by_id[candidate.user_id] = candidate
        self._id_by_username[candidate.username] = candidate.user_id
        self._id_by_email[candidate.email] = candidate.user_id
        self._next_user_id += 1
        return candidate

    def get_by_id(self, user_id: int) -> User:
        normalized_id = _validate_user_id(user_id)
        try:
            return self._users_by_id[normalized_id]
        except KeyError as exc:
            raise UserNotFoundError(f"user_id {normalized_id} is not registered") from exc

    def get_by_username(self, username: str) -> User:
        normalized = normalize_username(username)
        try:
            user_id = self._id_by_username[normalized]
        except KeyError as exc:
            raise UserNotFoundError(f"username '{normalized}' is not registered") from exc
        return self._users_by_id[user_id]

    def get_by_email(self, email: str) -> User:
        normalized = normalize_email(email)
        try:
            user_id = self._id_by_email[normalized]
        except KeyError as exc:
            raise UserNotFoundError(f"email '{normalized}' is not registered") from exc
        return self._users_by_id[user_id]

    def list_by_status(self, status: UserStatus) -> tuple[User, ...]:
        if not isinstance(status, UserStatus):
            raise TypeError("status must be a UserStatus")
        return tuple(user for user in self.users if user.status is status)

    def search(self, query: str, *, status: UserStatus | None = None) -> tuple[User, ...]:
        """Search canonical identity fields and optionally filter by account status."""
        normalized_query = _normalize_unicode(query, "query").strip().casefold()
        if not normalized_query:
            raise ValueError("query cannot be blank")
        if status is not None and not isinstance(status, UserStatus):
            raise TypeError("status must be a UserStatus or None")

        matches: list[User] = []
        for user in self.users:
            if status is not None and user.status is not status:
                continue
            haystack = (user.full_name.casefold(), user.username, user.email)
            if any(normalized_query in value for value in haystack):
                matches.append(user)
        return tuple(matches)

    def change_username(self, user_id: int, username: str) -> User:
        current = self.get_by_id(user_id)
        normalized = normalize_username(username)
        if normalized == current.username:
            return current

        self._ensure_identity_available(
            normalized,
            current.email,
            excluding_user_id=current.user_id,
        )
        updated = replace(current, username=normalized)

        del self._id_by_username[current.username]
        self._id_by_username[updated.username] = updated.user_id
        self._users_by_id[updated.user_id] = updated
        return updated

    def change_email(self, user_id: int, email: str) -> User:
        current = self.get_by_id(user_id)
        normalized = normalize_email(email)
        if normalized == current.email:
            return current

        self._ensure_identity_available(
            current.username,
            normalized,
            excluding_user_id=current.user_id,
        )
        updated = replace(current, email=normalized)

        del self._id_by_email[current.email]
        self._id_by_email[updated.email] = updated.user_id
        self._users_by_id[updated.user_id] = updated
        return updated

    def change_full_name(self, user_id: int, full_name: str) -> User:
        current = self.get_by_id(user_id)
        normalized = normalize_full_name(full_name)
        if normalized == current.full_name:
            return current

        updated = replace(current, full_name=normalized)
        self._users_by_id[updated.user_id] = updated
        return updated

    def _transition(
        self,
        user_id: int,
        *,
        allowed_from: tuple[UserStatus, ...],
        target: UserStatus,
    ) -> User:
        current = self.get_by_id(user_id)
        if current.status not in allowed_from:
            allowed = ", ".join(status.value for status in allowed_from)
            raise InvalidUserTransitionError(
                f"cannot transition user {user_id} from {current.status.value} to "
                f"{target.value}; allowed source states: {allowed}"
            )

        updated = replace(current, status=target)
        self._users_by_id[updated.user_id] = updated
        return updated

    def suspend(self, user_id: int) -> User:
        return self._transition(
            user_id,
            allowed_from=(UserStatus.ACTIVE,),
            target=UserStatus.SUSPENDED,
        )

    def reactivate(self, user_id: int) -> User:
        return self._transition(
            user_id,
            allowed_from=(UserStatus.SUSPENDED,),
            target=UserStatus.ACTIVE,
        )

    def deactivate(self, user_id: int) -> User:
        return self._transition(
            user_id,
            allowed_from=(UserStatus.ACTIVE, UserStatus.SUSPENDED),
            target=UserStatus.DEACTIVATED,
        )
