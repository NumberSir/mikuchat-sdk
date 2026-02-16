from ._api import Yuuz12Api


class BaiduCensor(Yuuz12Api):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["baidu", "img_censor"],
            key_name="censor_imgcensor",
            **kwargs
        )


__all__ = [
    "BaiduCensor"
]