from ._api import MikuChatApi


class Bangumi(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["Bangumi"],
            key_name="Bangumi",
            **kwargs
        )


__all__ = [
    "Bangumi"
]
