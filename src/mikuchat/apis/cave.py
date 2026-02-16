from ._api import Yuuz12Api


class Cave(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["cave"],
            key_name="cave",
            **kwargs
        )


__all__ = [
    "Cave"
]
