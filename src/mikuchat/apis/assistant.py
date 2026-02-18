from ._api import MikuChatApi


class Assistant(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["Assistant", "Qwen"],
            key_name="Assistant_Qwen",
            **kwargs
        )


__all__ = [
    "Assistant"
]