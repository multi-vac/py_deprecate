import logging
from typing import Callable
from py_deprecate.behaviors.base import BaseBehavior

logger = logging.getLogger(__name__)


class Log(BaseBehavior):
    def execute(self, message: str, func: Callable, *args, **kwargs):
        logger.warn(f"[DeprecationIntroduced]: Deprecated {func} called: {message}")
