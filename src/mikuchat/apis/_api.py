"""https://doc.yuuz12.top/web/#/5/23"""
from json import JSONDecodeError

import httpx
from loguru import logger

from ..config import get_config
from ..models import ResponseModel
from ..exceptions import MissingApiKeyException


class MikuChatApi:
	"""
	Provides an interface for interacting with the MikuChat API.

	This class allows asynchronous API calls and provides access to response data and status.

	Parameters
	----------
	client : httpx.AsyncClient, optional
		An instance of httpx.AsyncClient for making HTTP requests.
	version : int, optional
		The API version to use.
	nodes : list of str, optional
		A list of API endpoint nodes.
	key_name : str, optional
		The key name to extract results from the API response.

	Attributes
	----------
	BASE_URL_BOT : str
		Base URL for bot API.
	BASE_URL_FST : str
		Base URL for skin API.
	"""

	BASE_URL_BOT = "https://bot.miku.chat/api"
	BASE_URL_FST = "https://skin.fstmc.top/api"

	def __init__(self, client: httpx.AsyncClient = httpx.AsyncClient(), version: int = get_config().api_version, nodes: list[str] = None, key_name: str = None):
		self._client = client

		self._version = version
		self._nodes: list[str] = nodes or []  # ['user'], ['user', 'check']
		self._base_url = f"{self.BASE_URL_BOT}/v{self._version}/{'/'.join(self._nodes)}"

		self._key_name: str = key_name
		self._response: httpx.Response = None
		self._model: ResponseModel = None
		self._raw_content: bytes = None
		self._raw_json: dict = {}
		self._raw_code: int = None
		self._raw_msg: str = None
		self._result_json: dict = {}

	def call_api(self, api_name: str):
		"""
		Returns an asynchronous function to call a specific API endpoint.

		The returned function allows making GET or POST requests to the specified API and updates the instance with the response data.

		Parameters
		----------
		api_name : str
			The name of the API endpoint to call.

		Returns
		-------
		Callable
			An asynchronous function that performs the API request and returns an httpx.Response object.

		Raises
		------
		TypeError
			If an unsupported HTTP method is provided.
		"""
		async def _(method: str = "GET", **kwargs) -> httpx.Response:
			"""
			通用请求 API。

			该异步函数根据指定的 HTTP 方法和参数请求 API，并更新实例的响应数据。

			Parameters
			----------
			method : str, optional
				请求方法，支持 "GET" 或 "POST"，默认为 "GET"。
			**kwargs
				传递给请求的额外参数。

			Returns
			-------
			httpx.Response
				API 的响应对象。

			Raises
			------
			TypeError
				如果提供了不支持的 HTTP 方法。
			"""
			url = f"{self._base_url}/{api_name}"
			try:
				kwargs |= {"key": get_config().api_key[self._version]}
			except KeyError as e:
				raise MissingApiKeyException

			match method:
				case "GET":
					response = await self._client.get(url, params=kwargs, follow_redirects=True)
				case "POST":
					response = await self._client.post(url, data=kwargs, follow_redirects=True)
				case _:
					raise TypeError(f"Unsupported method {method} in API call")

			logger.debug(f"\nMikuChatApi called: {response.url}")
			self._response = response
			self._raw_content = self.response.content
			try:
				self._raw_json = self._response.json()
				if self._raw_json:
					self._result_json = self._raw_json[self._key_name]
					self._raw_code = self._raw_json["code"]
					self._raw_msg = self._raw_json["msg"]
					self._model = ResponseModel.model_validate(self._raw_json)
			except (UnicodeDecodeError, KeyError, JSONDecodeError) as e:  # 无 json
				self._raw_json = {}
				self._result_json = {}
			return response
		return _

	def __getattr__(self, api_name: str):
		return self.call_api(api_name)

	@property
	def response(self) -> httpx.Response:
		return self._response

	@property
	def model(self) -> ResponseModel:
		return self._model

	@property
	def raw(self) -> bytes:
		return self._raw_content

	@property
	def raw_data(self) -> dict:
		return self._raw_json

	@property
	def raw_msg(self) -> str:
		return self._raw_msg

	@property
	def raw_code(self) -> int:
		return self._raw_code

	@property
	def data(self) -> dict:
		return self._result_json

	@property
	def error(self) -> bool:
		return self.raw_code != 200


__all__ = [
	"MikuChatApi"
]
