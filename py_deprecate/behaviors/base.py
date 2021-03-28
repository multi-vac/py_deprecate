from abc import ABC
from typing import Callable


class BaseBehavior(ABC):
    def execute(self, message: str, func: Callable, *args, **kwargs):
        raise NotImplementedError
