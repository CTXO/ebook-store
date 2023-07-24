from .checkout_controller import CheckoutController
from .library_controller import LibraryController
from .signup_controller import SignupController


class Facade:
    def signup(self, full_name, email, password, password2):
        return SignupController().signup(full_name, email, password, password2)

    def checkout(self, payment_info):
        return CheckoutController().checkout(payment_info)

    def list_ebooks(self, user_id):
        return LibraryController().list_ebooks(user_id)

