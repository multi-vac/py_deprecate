import logging
from py_deprecate.behaviors.base import BaseBehavior

logger = logging.getLogger(__name__)


class Log(BaseBehavior):
    def execute(self, message: str):
        logger.warn(f"[DeprecationIntroduced]: {message}")
