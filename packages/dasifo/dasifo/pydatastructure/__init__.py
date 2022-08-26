import abc

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