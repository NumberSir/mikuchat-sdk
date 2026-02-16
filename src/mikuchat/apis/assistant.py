from ._api import Yuuz12Api


class Assistant(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["Assistant", "Qwen"],
            key_name="Assistant_Qwen",
            **kwargs
        )


__all__ = [
    "Assistant"
]