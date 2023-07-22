from .interface import IPSP
from .pagarme_controller import PagarmeController
from ..helpers.payment_info import PaymentInfo


class PSPFacade(IPSP):
    controller = PagarmeController()

    def checkout(self, payment_info: PaymentInfo):
        return self.controller.checkout(payment_info)

    def payment_succeeded(self, user_id: int, ebook_ids: list[int]):
        return self.controller.payment_succeeded(user_id=user_id, ebook_ids=ebook_ids)

