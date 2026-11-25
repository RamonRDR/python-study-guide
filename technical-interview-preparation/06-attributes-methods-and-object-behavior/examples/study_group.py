"""Demonstrate instance, class and static methods."""


class StudyGroup:
    category = "study"

    def __init__(self, label: str) -> None:
        if not self.valid_label(label):
            raise ValueError("label cannot be blank")
        self.label = label
        self.members: list[str] = []

    def add(self, member: str) -> None:
        self.members.append(member)

    @classmethod
    def from_label(cls, label: str):
        return cls(label.strip())

    @staticmethod
    def valid_label(label: str) -> bool:
        return isinstance(label, str) and bool(label.strip())

    def __len__(self) -> int:
        return len(self.members)

    def __str__(self) -> str:
        return f"{self.label}: {len(self)}"

    def __repr__(self) -> str:
        return f"StudyGroup(label={self.label!r}, members={self.members!r})"


if __name__ == "__main__":
    group = StudyGroup.from_label(" Python ")
    group.add("Ada")
    print(group)
