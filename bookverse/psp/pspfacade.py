from .interface import IPSP
from .pagarme_controller import PagarmeController
from ..helpers.payment_info import PaymentInfo


class PSPFacade(IPSP):
    controller: IPSP = PagarmeController()

    def checkout(self, payment_info: PaymentInfo):
        return self.controller.checkout(payment_info)

    def payment_succeeded(self, webhook_data: dict):
        return self.controller.payment_succeeded(webhook_data)

    def get_webhook_data(self, webhook_request) -> dict:
        return self.controller.get_webhook_data(webhook_request)

