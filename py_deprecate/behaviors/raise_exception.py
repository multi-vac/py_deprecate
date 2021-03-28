from py_deprecate.behaviors.base import BaseBehavior
from py_deprecate.exceptions import DeprecationIntroduced


class RaiseException(BaseBehavior):
    def execute(self, message: str):
        raise DeprecationIntroduced(message)
