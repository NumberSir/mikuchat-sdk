from ._api import MikuChatApi


class User(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["user"],
            key_name="user",
            **kwargs
        )


class UserCheck(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["user", "check"],
            key_name="user_check",
            **kwargs
        )


__all__ = [
    'User',
    "UserCheck"
]
