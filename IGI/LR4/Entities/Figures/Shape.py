import abc
from abc import ABC


class Shape(ABC):
    @abc.abstractmethod
    def get_area(self):
        pass
    