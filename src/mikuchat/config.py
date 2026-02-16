from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="YUUZ12_")

    api_version: int = Field(default=2)
    api_key: dict[int, str] = Field(default_factory=dict)


config = Config()


__all__ = [
    "config",
    "Config",
]


if __name__ == '__main__':
    print(config.model_dump())