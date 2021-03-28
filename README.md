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
