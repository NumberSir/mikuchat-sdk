from ._api import Yuuz12Api


class Prize(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["Prize"],
            key_name="Prize",
            **kwargs
        )


__all__ = [
    "Prize"
]