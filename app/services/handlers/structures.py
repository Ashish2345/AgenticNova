from abc import ABCMeta, abstractmethod


class AbstractHandler(metaclass=ABCMeta):

    @property
    def __classname__(self) -> str:
        return self.__class__.__name__

    def __call__(self, *args, **kwargs):
        return self.handler(*args, **kwargs)

    @abstractmethod
    def handler(self, *args, **kwargs):
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.__classname__} || {self.__dict__}"

    def __repr__(self):
        return str(self)

class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        re_init = kwargs.pop('force_reinit', False)
        if (cls not in cls._instances) or re_init:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]