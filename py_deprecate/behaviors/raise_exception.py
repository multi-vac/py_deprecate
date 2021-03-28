from typing import Callable

from py_deprecate.behaviors.base import BaseBehavior
from py_deprecate.exceptions import DeprecationIntroduced


class RaiseException(BaseBehavior):
    def execute(self, message: str, func: Callable, *args, **kwargs):
        raise DeprecationIntroduced(message)
