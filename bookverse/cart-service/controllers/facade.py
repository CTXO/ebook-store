from .ebook_controller import EbookController
from .cart_controller import CartController


class Facade:
    def list_available_ebooks(self, user_id):
        return EbookController().list_available_ebooks(user_id)

    def add_to_cart(self, user_id, ebook_id):
        return CartController().add_to_cart(user_id, ebook_id)

    def list_cart_ebooks(self, user_id):
        return CartController().list_ebooks(user_id)