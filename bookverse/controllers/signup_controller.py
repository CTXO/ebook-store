
from ..helpers.user_info import UserInfo
from .signup_handlers import HandlerRequest
from .signup_handlers import HandlerResponse
from .signup_handlers import SignupHandler
from ..cart.cart_crud import CartCrud
from ..library.library_crud import LibraryCrud
from ..user.user_crud import UserCrud
from werkzeug.security import generate_password_hash


class SignupController:
    def __init__(self):
        self.user_crud = UserCrud()
        self.cart_crud = CartCrud()
        self.library_crud = LibraryCrud()
        self.signup_handler = SignupHandler()

    def signup(self, full_name, email, password, password2) -> HandlerResponse:
        user_info = UserInfo(name=full_name, email=email, password=password, password2=password2)
        handler_request = HandlerRequest(user_info=user_info, user_crud=self.user_crud, cart_crud=self.cart_crud,
                                         library_crud=self.library_crud)
        signup_response = self.signup_handler.handle(handler_request)
        return signup_response
