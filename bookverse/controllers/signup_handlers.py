from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import TypedDict
from werkzeug.security import generate_password_hash

from ..user.models import User
from ..cart.cart_crud import CartCrud
from ..library.library_crud import LibraryCrud
from ..user.user_crud import UserCrud


class HandlerRequest:
    def __init__(self, name: str, email: str, password: str, password2: str,
                 user_crud: UserCrud, cart_crud: CartCrud, library_crud: LibraryCrud,
                 password_hash: Optional[str] = None, user: Optional[User] = None):
        self.name = name
        self.email = email
        self.password = password
        self.password2 = password2
        self.user_crud = user_crud
        self.cart_crud = cart_crud
        self.library_crud = library_crud
        self.user = user
        self.password_hash = password_hash


class HandlerResponse(TypedDict):
    success: bool
    message: str
    user: Optional[User]


class IHandler(ABC):
    @property
    @abstractmethod
    def next_handler(self):
        raise NotImplementedError

    @abstractmethod
    def handle(self, request: HandlerRequest) -> HandlerResponse:
        raise NotImplementedError


class LibraryCreationHandler(IHandler):
    next_handler = None

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        request.library_crud.create_library(request.user.id)
        return {"success": True, "message": None, "user": request.user}


class CartCreationHandler(IHandler):
    next_handler = LibraryCreationHandler()

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        request.cart_crud.create_cart(request.user.id)
        return self.next_handler.handle(request)


class UserCreationHandler(IHandler):
    next_handler = CartCreationHandler()

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        new_user = request.user_crud.create(request.name, request.email, request.password_hash)
        if not new_user:
            return {"success": False, "message": "Erro ao criar usuário", "user": None}
        request.user = new_user
        return self.next_handler.handle(request)


class PasswordValidationHandler(IHandler):
    next_handler = UserCreationHandler()

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        password = request.password
        password2 = request.password2
        if len(password) < 8:
            return {"success": False, "message": "Senha deve ter no mínimo 8 caracteres", "user": None}
        if password2 != password:
            return {"success": False, "message": "Senhas não conferem", "user": None}

        request.password_hash = generate_password_hash(password)
        return self.next_handler.handle(request)


class EmailValidationHandler(IHandler):
    next_handler = PasswordValidationHandler()

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        email = request.email
        existing_email = request.user_crud.retrieve_by_email(email)
        if existing_email:
            return {"success": False, "message": "Email já cadastrado", "user": None}
        return self.next_handler.handle(request)


class SignupHandler(IHandler):
    next_handler = EmailValidationHandler()

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        return self.next_handler.handle(request)




