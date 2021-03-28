import logging
import inspect

from typing import Callable, Iterable, Union
from functools import wraps

from .settings import default_behavior


def deprecated(allowed_deprecations: Union[Callable, Iterable], message: str = ""):
    if callable(allowed_deprecations):
        allowed_deprecations = allowed_deprecations()

    behavior = default_behavior

    def _deprecated_decorator(func: Callable):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            stack = inspect.stack()
            caller_stack = stack[1]
            for allowed_callable in allowed_deprecations:
                if caller_stack.frame.f_code == allowed_callable.__code__:
                    return func(*args, **kwargs)
            default_behavior().execute(message)
        return wrapped_func
    return _deprecated_decorator
