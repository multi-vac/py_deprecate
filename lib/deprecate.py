import logging
import inspect

from typing import List, Callable, Any
from functools import wraps

from lib.exceptions import ShitListedCallableCalled

logger = logging.getLogger(__name__)



def deprecated(shitlist: List[str], message: str = ""):
    def _deprecated_decorator(func: Callable):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            stack = inspect.stack()
            caller_name = stack[1].function

            if caller_name not in shitlist:
                raise ShitListedCallableCalled(message)

            return func(*args, **kwargs)
        return wrapped_func
    return _deprecated_decorator


@deprecated(shitlist=["give_me_sum_one"], message="Deprecated, please use sum2.")
def sum(a: int, b: int) -> int:
    return a + b

def give_me_sum(a: Any, b: Any) -> Any:
    return sum(a, b)

    # TODO - Support other types later.

class Sum:
    def give_me_sum_one(self, a: Any, b: Any) -> Any:
        return sum(a, b)

if __name__ == "__main__":
    print("Answer is", Sum().give_me_sum_one(5, 10))
    print("Answer is", give_me_sum(5, 10))