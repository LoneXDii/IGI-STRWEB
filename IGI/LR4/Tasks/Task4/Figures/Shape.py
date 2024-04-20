import abc
from abc import ABC
from Tasks.MyMixin import MyMixin


class Shape(ABC, MyMixin):
    @abc.abstractmethod
    def get_area(self):
        pass
    