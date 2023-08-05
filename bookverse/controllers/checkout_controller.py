from ..library.library_crud import LibraryCrud
from ..psp.interface import IPSP
from ..helpers.payment_info import PaymentInfo
from ..psp.pspfacade import PSPFacade


class CheckoutController:
    psp_facade: IPSP = PSPFacade()
    library_crud = LibraryCrud()

    def checkout(self, payment_info: PaymentInfo):
        return PSPFacade().checkout(payment_info)

    def add_ebook(self, user_id, ebook_id):
        self.library_crud.add_to_library(user_id=user_id, ebook_id=ebook_id)

