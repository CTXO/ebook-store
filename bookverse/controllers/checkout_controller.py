from ..helpers.payment_info import PaymentInfo
from ..psp.pspfacade import PSPFacade


class CheckoutController:
    def checkout(self, payment_info: PaymentInfo):
        return PSPFacade().checkout(payment_info)
