from ._api import Yuuz12Api
from ..models import ResponseModel

class Bangumi(Yuuz12Api):
    """番剧搜索"""
    def __init__(self, **kwargs): super().__init__(**kwargs)
    """搜索"""
    async def subject_search(self, keyword: str): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...
    @property
    def model(self) -> "ResponseModel": ...