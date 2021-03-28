import logging
import inspect

from typing import Callable, Iterable, Union
from functools import wraps

from lib.exceptions import ShitListedCallableCalled
logger = logging.getLogger(__name__)


def deprecated(allowed_deprecations: Union[Callable, Iterable], message: str = ""):
    if isinstance(allowed_deprecations, Callable):
        allowed_deprecations = allowed_deprecations()

    def _deprecated_decorator(func: Callable):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            stack = inspect.stack()
            caller_stack = stack[1]
            for allowed_callable in allowed_deprecations:
                if caller_stack.frame.f_code == allowed_callable.__code__:
                    return func(*args, **kwargs)
            raise ShitListedCallableCalled(message)
        return wrapped_func
    return _deprecated_decorator