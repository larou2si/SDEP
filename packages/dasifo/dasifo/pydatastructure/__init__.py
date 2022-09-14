import abc
from re import T

class PyList(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'add') and callable(subclass.add)

                or NotImplemented)

    @abc.abstractmethod
    def add(self) -> list:
        """  """
        raise NotImplementedError



class Tableau(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'append') and callable(subclass.append) and
                hasattr(subclass, 'pop') and callable(subclass.pop)

                or NotImplemented)

    @abc.abstractmethod
    def append(self) -> int:
        """ 
        return: int: the lenght of this list after addition of new element
        """
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self) -> T:
        """  """
        raise NotImplementedError