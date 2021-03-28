from typing import Any, List
from py_deprecate import deprecated, Disabled


def allowed_function(a: int, b: int) -> int:
    return deprecated_sum(a, b)


def forbidden_function(a: int, b: int) -> int:
    return deprecated_sum(a, b)


class TestClass:
    def allowed_instance_method(self, a: int, b: int) -> int:
        return deprecated_sum(a, b)

    def forbidden_instance_method(self, a: int, b: int) -> int:
        return deprecated_sum(a, b)

    @staticmethod
    def allowed_static_method(a: int, b: int) -> int:
        return deprecated_sum(a, b)

    @staticmethod
    def forbidden_static_method(a: int, b: int) -> int:
        return deprecated_sum(a, b)

    @classmethod
    def allowed_class_method(cls, a: int, b: int) -> int:
        return deprecated_sum(a, b)

    @classmethod
    def forbidden_class_method(cls, a: int, b: int) -> int:
        return deprecated_sum(a, b)


allowed_lambda = lambda a, b: deprecated_sum(a, b)
forbidden_lambda = lambda a, b: deprecated_sum(a, b)


@deprecated(
    allowed_deprecations=[
        allowed_function,
        TestClass.allowed_instance_method,
        TestClass.allowed_static_method,
        TestClass.allowed_class_method,
        allowed_lambda,
    ],
    message="Test message",
)
def deprecated_sum(a: Any, b: Any) -> Any:
    return a + b


def get_allowed_deprecations() -> List:
    return [allowed_func_caller]


def allowed_func_caller():
    func_with_decorator_using_a_callable()


def forbidden_func_caller():
    func_with_decorator_using_a_callable()


@deprecated(allowed_deprecations=get_allowed_deprecations)
def func_with_decorator_using_a_callable() -> str:
    return "Hello world!"


@deprecated(allowed_deprecations=[], message="Deprecate func", behavior=Disabled)
def deprecated_with_custom_behavior():
    return "Hello world!"
