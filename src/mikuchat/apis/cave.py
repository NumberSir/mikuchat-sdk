from ._api import MikuChatApi


class Cave(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["cave"],
            key_name="cave",
            **kwargs
        )


__all__ = [
    "Cave"
]
