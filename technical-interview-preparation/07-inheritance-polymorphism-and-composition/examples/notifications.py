"""Dispatch messages without depending on external services."""


class Channel:
    def send(self, message: str) -> str:
        raise NotImplementedError("subclasses must implement send")


class TextChannel(Channel):
    def send(self, message: str) -> str:
        return f"text: {message}"


class EmailChannel(Channel):
    def send(self, message: str) -> str:
        return f"email: {message}"


class Notifier:
    def __init__(self, channel) -> None:
        self.channel = channel

    def notify(self, message: str) -> str:
        return self.channel.send(message)


if __name__ == "__main__":
    print(Notifier(TextChannel()).notify("Ready"))
    print(Notifier(EmailChannel()).notify("Ready"))
