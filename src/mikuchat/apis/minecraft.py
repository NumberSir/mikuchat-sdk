from ._api import MikuChatApi


class MinecraftPing(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["minecraft"],
            key_name="minecraft_ping",
            **kwargs
        )


class MinecraftServer(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["minecraft", "server"],
            key_name="minecraft_server",
            **kwargs
        )


class MinecraftBlacklist(MikuChatApi):
    def __init__(self, **kwargs):
        super().__init__(
            nodes=["minecraft", "blacklist"],
            key_name="minecraft_blacklist",
            **kwargs
        )


__all__ = [
    "MinecraftPing",
    "MinecraftServer",
    "MinecraftBlacklist"
]
