from ._api import Yuuz12Api


class User(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["user"],
            key_name="user",
            **kwargs
        )


class UserCheck(Yuuz12Api):
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
