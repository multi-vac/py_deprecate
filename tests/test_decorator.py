from unittest import TestCase
from tests.fixtures import (
    allowed_deprecated_sum_caller,
    not_allowed_deprecated_sum_caller,
    TestClass,
    allowed_lambda,
    not_allowed_lambda,
)
from py_deprecate.exceptions import DeprecationIntroduced


class DeprecatedDecoratorTests(TestCase):
    def test_deprecated_function_called_from_function(self):
        # Call allowed deprecated and see nothing happens
        allowed_deprecated_sum_caller(5, 10)

        # But calling a function that's not allowed will raise error
        with self.assertRaises(DeprecationIntroduced):
            not_allowed_deprecated_sum_caller(5, 10)

    def test_deprecated_function_called_from_method_instance(self):
        # Nothing happens when called with method instance
        TestClass().allowed_instance_method(5, 10)

        # But calling a method instance that's not allowe will raise error
        with self.assertRaises(DeprecationIntroduced):
            TestClass().not_allowed_instance_method(5, 10)

    def test_deprecated_function_called_from_staticmethod(self):
        # Nothing happens when called from allowed staticmethod
        TestClass.allowed_static_method(5, 10)

        # But calling the not allowed static method raises the exception
        with self.assertRaises(DeprecationIntroduced):
            TestClass.not_allowed_static_method(5, 10)

    def test_deprecated_function_called_from_classmethod(self):
        # Nothing happens when called from allowed classmethod
        TestClass.allowed_class_method(5, 10)

        # But calling the not allowed static method raises the exception
        with self.assertRaises(DeprecationIntroduced):
            TestClass.not_allowed_class_method(5, 10)

    def test_deprecated_function_called_from_lambda(self):
        # Nothing happens when called from allowed lamda
        allowed_lambda(5, 10)

        # But calling the not allowed static method raises the exception
        with self.assertRaises(DeprecationIntroduced):
            not_allowed_lambda(5, 10)
