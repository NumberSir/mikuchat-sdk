from ._api import MikuChatApi


class Prize(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["Prize"],
            key_name="Prize",
            **kwargs
        )


__all__ = [
    "Prize"
]