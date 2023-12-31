from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import TypedDict
from werkzeug.security import generate_password_hash

from ..user_info import UserInfo
from ..models.models import User
from ..user_crud import UserCrud


class HandlerRequest:
    def __init__(self, user_info: UserInfo, user_crud: UserCrud, cart_crud, library_crud,
                 password_hash: Optional[str] = None, user: Optional[User] = None):
        self.user_info = user_info
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
    @abstractmethod
    def handle(self, request: HandlerRequest) -> HandlerResponse:
        raise NotImplementedError

class UserCreationHandler(IHandler):
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        name = request.user_info.name
        email = request.user_info.email
        new_user = request.user_crud.create(name, email, request.password_hash)
        if not new_user:
            return {"success": False, "message": "Erro ao criar usuário", "user": None}
        request.user = new_user
        if not self.next_handler:
            return {"success": True, "message": None, "user": new_user}
        return self.next_handler.handle(request)


class PasswordValidationHandler(IHandler):
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        password = request.user_info.password
        password2 = request.user_info.password2
        if len(password) < 8:
            return {"success": False, "message": "Senha deve ter no mínimo 8 caracteres", "user": None}
        if password2 != password:
            return {"success": False, "message": "Senhas não conferem", "user": None}

        request.password_hash = generate_password_hash(password)
        return self.next_handler.handle(request)


class EmailValidationHandler(IHandler):
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        email = request.user_info.email
        existing_email = request.user_crud.retrieve_by_email(email)
        if existing_email:
            return {"success": False, "message": "Email já cadastrado", "user": None}
        return self.next_handler.handle(request)


class SignupHandler(IHandler):
    def __init__(self, next_handler):
        self.next_handler = next_handler

    def handle(self, request: HandlerRequest) -> HandlerResponse:
        return self.next_handler.handle(request)




