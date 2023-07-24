from ..cart.cart_crud import CartCrud
from ..library.library_crud import LibraryCrud
from ..user.user_crud import UserCrud
from werkzeug.security import generate_password_hash, check_password_hash

class LoginController:
    user_crud = UserCrud()  # TODO inject

    def __init__(self):
        self.user_crud = UserCrud()  # TODO inject this dependency
        self.cart_crud = CartCrud()
        self.library_crud = LibraryCrud()

    def login(self, email, password):
        existing_user = self.user_crud.retrieve_by_email(email)
        if not existing_user:
            return {"success": False, "message": "Email não cadastrado"}
        password_hash = generate_password_hash(password)
        if(existing_user.password_hash != password_hash):
            return {"success": False, "message": "Senha incorreta"}

        return {"success": True, "message": None, "user": existing_user}


