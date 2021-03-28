from abc import ABC


class BaseBehavior(ABC):
    def execute(self, message: str):
        raise NotImplementedError
