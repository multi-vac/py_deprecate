import logging
import inspect

from typing import Callable, Iterable, Union, Optional
from functools import wraps

from .settings import default_behavior
from py_deprecate.behaviors.base import BaseBehavior


def deprecated(
    allowed_deprecations: Union[Callable, Iterable],
    message: str = "",
    behavior: Optional[BaseBehavior] = None,
):
    if callable(allowed_deprecations):
        allowed_deprecations = allowed_deprecations()

    if not behavior:
        behavior = default_behavior

    def _deprecated_decorator(func: Callable):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            stack = inspect.stack()
            caller_stack = stack[1]
            for allowed_callable in allowed_deprecations:
                if caller_stack.frame.f_code == allowed_callable.__code__:
                    return func(*args, **kwargs)

            behavior().execute(message)

        return wrapped_func

    return _deprecated_decorator
