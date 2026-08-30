from user_registration import UserRegistry, UserStatus


def main() -> None:
    registry = UserRegistry()
    maya = registry.register("Maya Chen", "Maya.Chen", "MAYA@Example.com")
    noah = registry.register("Noah Rivera", "noah-r", "noah@example.org")
    registry.register("Lina Costa", "lina_c", "lina@example.net")

    registry.change_email(maya.user_id, "maya.chen@example.com")
    registry.suspend(noah.user_id)

    print(f"users: {len(registry.users)}")
    print(f"active: {len(registry.list_by_status(UserStatus.ACTIVE))}")
    print(f"suspended: {len(registry.list_by_status(UserStatus.SUSPENDED))}")
    print(f"lookup: {registry.get_by_email('MAYA.CHEN@EXAMPLE.COM').username}")
    print(f"search-example: {len(registry.search('example'))}")


if __name__ == "__main__":
    main()
