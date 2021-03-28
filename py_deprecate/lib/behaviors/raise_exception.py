from behavior.base import BaseBehavior
from lib.exceptions import DeprecationIntroduced


class RaiseException(BaseBehavior):
    def execute(self, message: str):
        raise DeprecationIntroduced(message)