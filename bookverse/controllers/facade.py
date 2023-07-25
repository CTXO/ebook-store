from .ebook_controller import EbookController
from .login_controller import LoginController
from .checkout_controller import CheckoutController
from .library_controller import LibraryController
from .signup_controller import SignupController
from .cart_controller import CartController


class Facade:
    def signup(self, full_name, email, password, password2):
        return SignupController().signup(full_name, email, password, password2)

    def login(self, email, password):
        return LoginController().login(email,password)

    def checkout(self, payment_info):
        return CheckoutController().checkout(payment_info)

    def list_library_ebooks(self, user_id):
        return LibraryController().list_library_ebooks(user_id)

    def list_available_ebooks(self, user_id):
        return EbookController().list_available_ebooks(user_id)

    def add_to_cart(self, user_id, ebook_id):
        return CartController().add_to_cart(user_id, ebook_id)

    def list_cart_ebooks(self, user_id):
        return CartController().list_ebooks(user_id)