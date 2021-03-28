from unittest import TestCase

from py_deprecate.behaviors.log import Log
from py_deprecate.exceptions import DeprecationIntroduced
from py_deprecate import settings


from tests.fixtures import (
    TestClass,
    allowed_function,
    allowed_lambda,
    forbidden_function,
    forbidden_lambda,
    allowed_func_caller,
    forbidden_func_caller,
    deprecated_with_custom_behavior,
)


class DeprecatedDecoratorTests(TestCase):
    def test_deprecated_function_called_from_function(self):
        # Call allowed deprecated and see nothing happens
        allowed_function(5, 10)

        # But calling a function that's not allowed will raise error
        with self.assertRaises(DeprecationIntroduced):
            forbidden_function(5, 10)

    def test_deprecated_function_called_from_method_instance(self):
        # Nothing happens when called with method instance
        TestClass().allowed_instance_method(5, 10)

        # But calling a method instance that's not allowe will raise error
        with self.assertRaises(DeprecationIntroduced):
            TestClass().forbidden_instance_method(5, 10)

    def test_deprecated_function_called_from_staticmethod(self):
        # Nothing happens when called from allowed staticmethod
        TestClass.allowed_static_method(5, 10)

        # But calling the not allowed static method raises the exception
        with self.assertRaises(DeprecationIntroduced):
            TestClass.forbidden_static_method(5, 10)

    def test_deprecated_function_called_from_classmethod(self):
        # Nothing happens when called from allowed classmethod
        TestClass.allowed_class_method(5, 10)

        # But calling the not allowed static method raises the exception
        with self.assertRaises(DeprecationIntroduced):
            TestClass.forbidden_class_method(5, 10)

    def test_deprecated_function_called_from_lambda(self):
        # Nothing happens when called from allowed lamda
        allowed_lambda(5, 10)

        # But calling the not allowed static method raises the exception
        with self.assertRaises(DeprecationIntroduced):
            forbidden_lambda(5, 10)

    def test_use_decorator_with_callable(self):
        # Nothing happens if allowed function is used
        allowed_func_caller()

        with self.assertRaises(DeprecationIntroduced):
            forbidden_func_caller()

    def test_override_default_behavior(self):
        # Use a caller that's not whitelisted, but the default
        # behavior is something set to log.
        response = deprecated_with_custom_behavior()
        self.assertEqual(response, "Hello world!")
