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
    """
    Decorator for marking code as deprecated.

    allowed_deprecations: Can either be a callable thats returns
        an iterable of allowed callables that are whitelisted to
        use the deprecated callable, or can be an iterable of
        callables.
    message: Used in behaviours if a non whitelisted callable uses
        the deprecated callable.
    behaviour: Specifies what happens if a non whitelisted callable
    uses the deprecated callable.
    """
    if callable(allowed_deprecations):
        allowed_deprecations = allowed_deprecations()

    # Get the default behavior if not specified
    if not behavior:
        behavior = default_behavior

    def _deprecated_decorator(func: Callable):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            # Get the stack of the caller
            stack = inspect.stack()
            caller_stack = stack[1]

            # Iterate over whitelisted callables and see if the caller
            # is one of them. If it's not, then call the specified
            # behavior to handle it. This works by comparing the bytecode
            # of the caller with callables whitelisted.
            for allowed_callable in allowed_deprecations:
                if caller_stack.frame.f_code == allowed_callable.__code__:
                    return func(*args, **kwargs)

            return behavior().execute(message, func, *args, **kwargs)

        return wrapped_func

    return _deprecated_decorator
