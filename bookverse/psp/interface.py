from abc import ABC
from abc import abstractmethod

from ..helpers.payment_info import PaymentInfo


class IPSP(ABC):
    @abstractmethod
    def checkout(self, payment_info: PaymentInfo):
        raise NotImplementedError

    @abstractmethod
    def payment_succeeded(self, webhook_data):
        raise NotImplementedError

    @abstractmethod
    def get_webhook_data(self, webhook_request):
        raise NotImplementedError

