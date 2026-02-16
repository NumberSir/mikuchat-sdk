from ._api import Yuuz12Api


class Statistics(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["statistics"],
            key_name="statistics",
            **kwargs
        )


__all__ = [
    "Statistics"
]
