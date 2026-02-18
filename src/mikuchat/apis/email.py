from ._api import MikuChatApi


class Email(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["email"],
            **kwargs
        )


__all__ = [
    "Email"
]
