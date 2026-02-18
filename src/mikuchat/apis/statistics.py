from ._api import MikuChatApi


class Statistics(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["statistics"],
            key_name="statistics",
            **kwargs
        )


__all__ = [
    "Statistics"
]
