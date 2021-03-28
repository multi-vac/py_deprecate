from typing import Callable
from py_deprecate.behaviors.base import BaseBehavior


class Disabled(BaseBehavior):
    def execute(self, message: str, func: Callable, *args, **kwargs):
        return func(*args, **kwargs)
