from ._api import Yuuz12Api


class Email(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["email"],
            **kwargs
        )


__all__ = [
    "Email"
]
