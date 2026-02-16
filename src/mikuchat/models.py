from datetime import date, datetime

from pydantic import BaseModel, Field


class AssistantModel(BaseModel, extra="allow"):
    """AI助手"""
    content: str | None = Field(default=None, description="返回内容")


class UserModel(BaseModel, extra="allow"):
    """用户数据"""
    class BadgeModel(BaseModel, extra="allow"):
        """徽章"""
        Enable: list[str] | None = Field(default=None)
        Disable: list[str] | None = Field(default=None)

    qq: int | None = Field(default=None, description="qq号")
    id: int | None = Field(default=None, description="用户id，按注册顺序排列")
    name: str | None = Field(default=None, description="用户昵称")
    kook_id: str | None = Field(default=None, description="kook号")
    telegram_name: str | None = Field(default=None, description="tg名称")
    osu_name: str | None = Field(default=None, description="osu名称")
    osu_mode: str | None = Field(default=None, description="osu模式")
    fst_email: str | None = Field(default=None, description="fst账号的邮箱")
    favorability: float | None = Field(default=None, description="好感度")
    coin: int | None = Field(default=None, description="硬币数")
    check_in_time_last: date | None = Field(default=None, description="上次签到日期，YYYY-MM-DD")
    check_number: int | None = Field(default=None, description="签到数")
    check_rank: int | None = Field(default=None, description="签到等级")
    status: int | None = Field(default=None, description="账号状态")
    group: int | None = Field(default=None, description="用户组")
    registered_time: datetime | None = Field(default=None, description="注册时间，YYYY-MM-DD hh:mm:ss")
    registered_timestamp: datetime | None = Field(default=None, description="注册时间戳")
    item: dict | None = Field(default_factory=dict, description="道具")
    badge: BadgeModel | None = Field(default=None, description="徽章")

    all_user_coin: int | None = Field(default=None, description="所有用户硬币之和")


class UserCheckModel(BaseModel, extra="allow"):
    """用户签到"""
    url: str | None = Field(default=None, description="上传图片链接")

    qq: int | None = Field(default=None, description="qq号")
    cover: str | None = Field(default=None, description="上传封面图链接")
    cover_status: int | None = Field(default=None, description="封面图审核状态")

    cover_blur: int | None = Field(default=None, description="封面图模糊状态")

    bottom: str | None = Field(default=None, description="上传背景图链接")
    bottom_status: int | None = Field(default=None, description="背景图审核状态")


class MinecraftPingModel(BaseModel, extra="allow"):
    """MC相关"""
    class MinecraftDescriptionModel(BaseModel, extra="allow"):
        class MinecraftDescriptionTextModel(BaseModel, extra="allow"):
            text: str | None = Field(default=None)
        extra: list[MinecraftDescriptionTextModel] | None = Field(default=None)
        text: str | None = Field(default=None)
    class MinecraftVersionModel(BaseModel, extra="allow"):
        name: str | None = Field(default=None, description="游戏版本名称")
        protocol: int | None = Field(default=None, description="游戏版本协议号")
    class MinecraftSampleModel(BaseModel, extra="allow"):
        id: str | None = Field(default=None, description="玩家UUID")
        name: str | None = Field(default=None, description="玩家昵称")
    class MinecraftForgedataModel(BaseModel, extra="allow"):
        class MinecraftForgedataChannelModel(BaseModel, extra="allow"):
            res: str | None = Field(default=None, description="模组命名空间相关")
            version: str | None = Field(default=None, description="模组版本相关")
            required: bool | None = Field(default=None, description="模组是否必需")
        channels: list[MinecraftForgedataChannelModel] | None = Field(default=None)
    class MinecraftModModel(BaseModel, extra="allow"):
        modId: str | None = Field(default=None, description="模组名称")
        modmarker: str | None = Field(default=None, description="对应MC版本")
    class MinecraftModInfoModel(BaseModel, extra="allow"):
        class MinecraftModModel(BaseModel, extra="allow"):
            modid: str | None = Field(default=None)
            version: str | None = Field(default=None)
        type: str | None = Field(default=None, description="模组加载器")
        modList: list[MinecraftModModel] | None = Field(default=None)

    description: MinecraftDescriptionModel | None = Field(default=None, description="服务器描述")
    max: int | None = Field(default=None, description="服务器最大人数")
    online: int | None = Field(default=None, description="服务器在线人数")
    version: MinecraftVersionModel | None = Field(default=None, description="游戏版本")
    sample: list[MinecraftSampleModel] | None = Field(default=None, description="玩家信息")
    forge_data: MinecraftForgedataModel | None = Field(default=None, description="Forge信息相关")
    mods: list[MinecraftModModel] | None = Field(default=None, description="模组信息相关")
    modInfo: MinecraftModInfoModel | None = Field(default=None, description="模组信息相关")
    favicon: str | None = Field(default=None, description="base64")


class MinecraftServerModel(BaseModel, extra="allow"):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None, description="以','隔开的服务器昵称")
    qq_group: str | None = Field(default=None, description="以','隔开的群号")
    host: str | None = Field(default=None)


class MinecraftBlacklistModel(BaseModel, extra="allow"):
    id: int | None = Field(default=None)
    qq: int | None = Field(default=None, description="常用QQ号")
    email: str | None = Field(default=None, description="常用邮箱")
    online_id: str | None = Field(default=None, description="常用正版昵称")
    normal_id: str | None = Field(default=None, description="常用第三方昵称")
    reason: str | None = Field(default=None, description="封禁原因")


class CaveModel(BaseModel, extra="allow"):
    """回声洞"""
    id: int | None = Field(default=None, description="回声编号")
    type: int | None = Field(default=None, description="回声类型")
    qq: int | None = Field(default=None, description="上传者qq号")
    string: str | None = Field(default=None, description="文字内容")
    image: str | None = Field(default=None, description="图片链接")
    time: date | None = Field(default=None, description="上传日期")

    url: str | None = Field(default=None, description="上传图片链接")


# class StatisticModel(BaseModel, extra="allow"):
#     id: int | None = Field(default=None)
#     group_id: int | None = Field(default=None)


class BaiduImageCensorModel(BaseModel, extra="allow"):
    type: int | None = Field(default=None, description="1-合规|2-不合规|3-疑似")
    probability: float | None = Field(default=None, description="疑似不合规的概率")


class PrizeModel(BaseModel, extra="allow"):
    qq: int | None = Field(default=None)
    awards: dict[str, int] | None = Field(default=None, description="奖励等级:中奖次数-6-没中奖|5-三等奖(45)|4-二等奖(1000)|3-一等奖(1500)|2-特等奖(20000)|1-特大等奖(100%)|0-奖池内货币不足(100%),重置500")
    user_coin: int | None = Field(default=None)
    all_coin: int | None = Field(default=None)
    last_time_attended: date | None = Field(default=None)

    coin: int | None = Field(default=None)


class ResponseModel(BaseModel, extra="allow"):
    """Api 返回值"""
    code: int | None = Field(default=None, description="状态码")
    msg: str | None = Field(default=None, description="状态信息|邮件发送成功")

    timer: float | None = Field(default=None, description="查询MC服务器返回时长")

    Assistant_Qwen: AssistantModel | None = Field(default=None, description="Assistant-Qwen")
    user: UserModel | list[UserModel] | None = Field(default=None, description="user-新建|获取数据|签到|更新数据|设置数据|道具")
    user_check: UserCheckModel | None = Field(default=None, description="user-check-上传图|更新状态")
    minecraft_ping: MinecraftPingModel | None = Field(default=None, description="minecraft-ping")
    minecraft_server: MinecraftServerModel | None = Field(default=None, description="minecraft-server-查询")
    minecraft_blacklist: MinecraftBlacklistModel | None = Field(default=None, description="minecraft-blacklist-查询|添加|删除")
    cave: CaveModel | None = Field(default=None, description="cave-获取|传入|更新|删除|恢复")
    censor_imgcensor: BaiduImageCensorModel | None = Field(default=None, description="图片色情内容审核")
    Prize: PrizeModel | list[PrizeModel] | None = Field(default=None, description="抽奖池")


__all__ = [
    "AssistantModel",
    "UserModel",
    "UserCheckModel",
    "MinecraftPingModel",
    "MinecraftServerModel",
    "MinecraftBlacklistModel",
    "CaveModel",
    "BaiduImageCensorModel",
    "PrizeModel",

    "ResponseModel",
]
