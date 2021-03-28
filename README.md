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
forbidden_sum_caller()

#>Traceback (most recent call last):
#>File "<stdin>", line 1, in <module>
#>File "<stdin>", line 2, in forbidden_sum_caller
#>File "/home/user/py_deprecate/decorate.py", line 50, in wrapped_func
#>  behavior().execute(message)
#>File "/home/user/py_deprecate/behaviors/raise_exception.py", line 7, in execute
#>  raise DeprecationIntroduced(message)
#>py_deprecate.exceptions.DeprecationIntroduced: sum is no longer supported.
```