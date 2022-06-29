from abc import ABC,  abstractmethod


class ISimplifier(ABC):
    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def simplify(self):
        pass
