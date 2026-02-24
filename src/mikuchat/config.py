from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
	model_config = SettingsConfigDict(
		env_prefix="MIKUCHAT_",
		env_file=".env",
		env_file_encoding="utf-8",
	)

	is_debug: bool = Field(default=False)
	api_version: int = Field(default=2)
	api_key: dict[int, str] = Field(default_factory=dict)

	@field_validator("api_version", mode="before")
	@classmethod
	def validate_api_version(cls, value: int, info: ValidationInfo):
		if info.data["is_debug"] or isinstance(value, int) or value.isdigit():
			return value
		raise ValueError("MIKUCHAT_API_VERSION 必须为正整数")

	@field_validator("api_key", mode="before")
	@classmethod
	def validate_api_key(cls, value: str, info: ValidationInfo):
		if info.data["is_debug"]:
			return value

		if not value:
			raise ValueError("尚未填写 MIKUCHAT_API_KEY 环境变量")

		if not isinstance(value, dict):
			raise ValueError("MIKUCHAT_API_KEY 必须为字典")

		return value


_config_instance: Config | None = None

def get_config() -> Config:
	"""全局实例"""
	global _config_instance
	if _config_instance is None:
		load_dotenv()
		_config_instance = Config()
	return _config_instance


def reload_config() -> Config:
	"""重载"""
	global _config_instance
	load_dotenv()
	_config_instance = Config()
	return _config_instance


__all__ = [
	"get_config",
	"reload_config",
	"Config",
]

if __name__ == '__main__':
	print(get_config().model_dump())