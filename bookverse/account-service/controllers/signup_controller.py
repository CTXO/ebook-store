from .signup_handlers import CartCreationHandler
from .signup_handlers import EmailValidationHandler
from .signup_handlers import LibraryCreationHandler
from .signup_handlers import PasswordValidationHandler
from .signup_handlers import UserCreationHandler
from .signup_handlers import HandlerRequest
from .signup_handlers import HandlerResponse
from .signup_handlers import SignupHandler
# from ..cart.cart_crud import CartCrud
# from ..library.library_crud import LibraryCrud
from ..user_crud import UserCrud
from ..user_info import UserInfo


class SignupController:
    def __init__(self):
        self.user_crud = UserCrud()
        # self.cart_crud = CartCrud()
        # self.library_crud = LibraryCrud()
        # self.library_handler = LibraryCreationHandler(None)
        # self.cart_handler = CartCreationHandler(self.library_handler)
        self.user_handler = UserCreationHandler(None)
        self.password_handler = PasswordValidationHandler(self.user_handler)
        self.email_handler = EmailValidationHandler(self.password_handler)
        self.signup_handler = SignupHandler(self.email_handler)

    def signup(self, full_name, email, password, password2) -> HandlerResponse:
        user_info = UserInfo(name=full_name, email=email, password=password, password2=password2)
        handler_request = HandlerRequest(user_info=user_info, user_crud=self.user_crud, cart_crud=None,
                                         library_crud=None)
        signup_response = self.signup_handler.handle(handler_request)
        return signup_response
