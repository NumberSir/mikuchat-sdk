import pytest

from ..apis.user import User
from ..apis.cave import Cave
from ..apis.minecraft import MinecraftPing
from ..models import MinecraftPingModel, UserModel, CaveModel


@pytest.fixture
def user() -> User: return User()
@pytest.fixture
def cave() -> Cave: return Cave()
@pytest.fixture
def minecraft_ping() -> MinecraftPing: return MinecraftPing()


@pytest.mark.asyncio
async def test_user_get_info(user: User):
    await user.get_user_info(qq=2596307102)
    user_model: UserModel = user.model.user
    assert user_model.qq == 2596307102
    assert user_model.name == "Number_Sir"
    assert user_model.group == 52
    assert user_model.fst_email == "2596307102"


@pytest.mark.asyncio
async def test_cave_get(cave: Cave):
    await cave.get_cave()
    cave_model: CaveModel = cave.model.cave
    assert isinstance(cave_model.id, int)
    match cave_model.type:
        case 0:  # text
            assert cave_model.string is not None
        case 1:  # image
            assert cave_model.string.find("https://bot.miku.chat/api/img-link/img/") != -1
        case 2:  # mixed
            assert cave_model.image is not None
        case _:
            assert ValueError


@pytest.mark.asyncio
async def test_minecraft_ping(minecraft_ping: MinecraftPing):
    await minecraft_ping.ping(ip='mccn.online', port=52101)
    minecraft_ping_model: MinecraftPingModel = minecraft_ping.model.minecraft_ping
    assert minecraft_ping_model.version is not None