# from ..cart.cart_crud import CartCrud
# from ..library.library_crud import LibraryCrud
from ..user_crud import UserCrud
from werkzeug.security import generate_password_hash, check_password_hash

class LoginController:
    user_crud = UserCrud()

    def __init__(self):
        self.user_crud = UserCrud()

    def login(self, email, password):
        existing_user = self.user_crud.retrieve_by_email(email)
        if not existing_user:
            return {"success": False, "message": "Email não cadastrado"}
        if not check_password_hash(existing_user.password_hash, password):
            return {"success": False, "message": "Senha incorreta"}

        return {"success": True, "message": None, "user": existing_user}


