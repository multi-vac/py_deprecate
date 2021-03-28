from py_deprecate.behaviors.base import BaseBehavior


class Disabled(BaseBehavior):
    def execute(self, message: str):
        pass
