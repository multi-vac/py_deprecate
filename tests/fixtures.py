from typing import Any
from py_deprecate.decorate import deprecated


def allowed_deprecated_sum_caller(a: int, b: int) -> int:
    return deprecated_sum(a, b)

def not_allowed_deprecated_sum_caller(a: int, b: int) -> int:
    return deprecated_sum(a, b)


class TestClass:
    def allowed_instance_method(self, a: int, b: int) -> int:
        return deprecated_sum(a, b)
    
    def not_allowed_instance_method(self, a: int, b: int) -> int:
        return deprecated_sum(a, b)
    
    @staticmethod
    def allowed_static_method(a: int, b: int) -> int:
        return deprecated_sum(a, b)
    
    @staticmethod
    def not_allowed_static_method(a: int, b: int) -> int:
        return deprecated_sum(a, b)
    
    @classmethod
    def allowed_class_method(cls, a: int, b: int) -> int:
        return deprecated_sum(a, b)
    
    @classmethod
    def not_allowed_class_method(cls, a: int, b: int) -> int:
        return deprecated_sum(a, b)


allowed_lambda = lambda a, b: deprecated_sum(a, b)
not_allowed_lambda = lambda a, b: deprecated_sum(a, b)

@deprecated(allowed_deprecations=[
    allowed_deprecated_sum_caller,
    TestClass.allowed_instance_method,
    TestClass.allowed_static_method,
    TestClass.allowed_class_method,
    allowed_lambda
    ], message="Test message")
def deprecated_sum(a: Any, b: Any) -> Any:
    return a + b
