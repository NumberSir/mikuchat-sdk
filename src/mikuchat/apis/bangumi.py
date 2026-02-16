from ._api import Yuuz12Api


class Bangumi(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["Bangumi"],
            key_name="Bangumi",
            **kwargs
        )


__all__ = [
    "Bangumi"
]
