from abc import ABC
from abc import abstractmethod

from .facade import Facade


class IPSP(ABC):
    facade = Facade()

    @abstractmethod
    def checkout(self):
        return self.facade.checkout()

    @abstractmethod
    def payment_succeeded(self):
        return self.facade.payment_succeeded()