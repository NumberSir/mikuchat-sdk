import sys

from loguru import logger as logger_


def _filter(record):
    return record["extra"].get("name") == "MikuChatApi"


logger_.add(
    sys.stdout,
    format="<g>{time:HH:mm:ss}</g> | [<lvl>{level}</lvl>] | {message}",
    colorize=True,
    filter=_filter
)

logger = logger_.bind(name="MikuChatApi")

__all__ = ["logger"]
