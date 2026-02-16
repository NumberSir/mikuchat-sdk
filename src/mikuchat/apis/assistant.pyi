from ._api import Yuuz12Api
from ..models import ResponseModel

class Assistant(Yuuz12Api):
    """AI聊天相关"""
    def __init__(self, **kwargs): super().__init__(**kwargs)
    """通义千问 - 长崎soyo"""
    async def Nagasaki_Soyo(self, user: str): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...
    @property
    def model(self) -> "ResponseModel": ...