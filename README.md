# Python Deprecation Toolkit


Python code deprecation toolkit for deprecating your Python code using a
[shitlist](https://sirupsen.com/shitlists/) approach.


## Installation

Install using `pip install py-deprecate`.

## Example

```py
from py_deprecate import deprecated
from py_deprecate.exceptions import DeprecationIntroduced

def allowed_sum_caller() -> int:
    return sum(5, 10)

def forbidden_sum_caller() -> int:
    return sum(5, 10)

# Only allowed_sum_caller is allowed to use sum.
@deprecated(
    allowed_deprecations=[allowed_sum_caller],
    message="sum is no longer supported."
)
def sum(a: int, b: int) -> int:
    return a + b

assert allowed_sum_caller() == 15

# Now, try with the function that's not whitelisted
try:
    forbidden_sum_caller()
except DeprecationIntroduced as exc:
    print("Caught deprecated exception!")
#> Caught deprecated exception!
```

## Behaviour

`py_deprcate` will raise an exception by default if a deprecated method
or function is called where it's not supposed to be called. This can be
overridden by specifying a behavior. Continuing from the example above:

```py
from py_deprecate import deprecated, Disabled

@deprecated(
    allowed_deprecations=[allowed_sum_caller],
    message="sum is no longer supported.",
    behavior=Disabled
)
def sum(a: int, b: int) -> int:
    return a + b

assert forbidden_sum_caller() == 15
```

Here we've disabled all the side effects by using `Disabled` behavior. By default
three behaviors are present: `Disabled`, `RaiseExeption`, and `Log`. You can also
write your own behaviors like this:

```py
from typing import Callable
from py_deprecate.behaviors.base import BaseBehavior

class CustomBehavior(BaseBehavior):
    def execute(self, message: str, func: Callable, *args, **kwargs):
        print("Custom behavior that will print this and raise Exception.")
        raise Exception

@deprecated(
    allowed_deprecations=[allowed_sum_caller],
    message="sum is no longer supported.",
    behavior=CustomBehavior
)
def sum(a: int, b: int) -> int:
    return a + b

forbidden_sum_caller()

#> Custom behavior that will print this and raise Exception.
#> Traceback (most recent call last):
#>  ...
#>  File "<stdin>", line 4, in execute
#> Exception
```

## Tests

Run the tests using `python -m unittest`.


## Resources

[Shitlist Driven Development](https://sirupsen.com/shitlists/) \
[This awesome Ruby gem that inspired me to create py_deprecate!](https://github.com/Shopify/deprecation_toolkit)

## License

Python Deprecation Toolkit is licensed under the [MIT License](https://github.com/multi-vac/py-deprecate/blob/master/LICENSE).


