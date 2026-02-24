import os
import pytest
from pydantic import ValidationError
from pydantic_settings import SettingsError

from mikuchat.config import Config


@pytest.fixture(autouse=True)
def clear_mikuchat_env(monkeypatch):
	for key in list(os.environ.keys()):
		if key.startswith("MIKUCHAT_"):
			monkeypatch.delenv(key, raising=False)
	yield


class TestConfig:
	def test_dotenv_prefix(self):
		"""测试环境变量前缀"""
		config = Config(is_debug=True)
		assert config.__class__.model_config.get("env_prefix") == "MIKUCHAT_", "环境变量前缀不为 MIKUCHAT_"

	def test_default_api_version(self):
		"""测试默认值"""
		config = Config(is_debug=True)
		assert config.api_version == 2, "默认 api_version 值不为 2"

	@pytest.mark.parametrize(
		"api_version, expected",
		[
			pytest.param("0", 0),
			pytest.param("1", 1),
		]
	)
	def test_value_api_version(self, monkeypatch, api_version, expected):
		"""测试对 api_version 正常赋值"""
		monkeypatch.setenv("MIKUCHAT_API_VERSION", api_version)
		monkeypatch.setenv("MIKUCHAT_API_KEY", '{"1":"api_key_v1","2":"api_key_v2"}')
		assert Config().api_version == expected

	@pytest.mark.parametrize(
		"api_version",
		[
			pytest.param("None"),
			pytest.param("a"),
			pytest.param("[]"),
			pytest.param("{}"),
			pytest.param("1.2"),
			pytest.param("True"),
		]
	)
	def test_exception_value_api_version(self, monkeypatch, api_version):
		"""测试对 api_version 的错误赋值"""
		monkeypatch.setenv("MIKUCHAT_API_VERSION", api_version)
		monkeypatch.setenv("MIKUCHAT_API_KEY", '{"1":"api_key_v1","2":"api_key_v2"}')
		with pytest.raises(ValidationError) as e:
			Config()

		assert e.type is ValidationError, "报错并非 ValidationError"

	@pytest.mark.parametrize(
		"api_key, expected",
		[
			pytest.param('{"0": "k0"}', {0: "k0"}),
		]
	)
	def test_value_api_key(self, monkeypatch, api_key, expected):
		"""测试对 api_key 正常赋值"""
		monkeypatch.setenv("MIKUCHAT_API_VERSION", "0")
		monkeypatch.setenv("MIKUCHAT_API_KEY", api_key)
		assert Config().api_key == expected

	@pytest.mark.parametrize(
		"api_key",
		[
			pytest.param("None"),
			pytest.param("a"),
			pytest.param("[]"),
			pytest.param("{}"),
			pytest.param("1.2"),
			pytest.param("True"),
		]
	)
	def test_exception_value_api_key(self, monkeypatch, api_key):
		"""测试对 api_key 错误赋值"""
		monkeypatch.setenv("MIKUCHAT_API_VERSION", "0")
		monkeypatch.setenv("MIKUCHAT_API_KEY", api_key)
		with pytest.raises((ValidationError, SettingsError)) as e:
			Config()

		assert e.type in(ValidationError, SettingsError), "报错并非 ValidationError 或 SettingsError"