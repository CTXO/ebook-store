from .interface import IPSP
from .pagarme_controller import PagarmeController
from ..helpers.payment_info import PaymentInfo


class PSPFacade(IPSP):
    controller = PagarmeController()

    def checkout(self, payment_info: PaymentInfo):
        return self.controller.checkout(payment_info)

    def payment_succeeded(self):
        return self.controller.payment_succeeded()

