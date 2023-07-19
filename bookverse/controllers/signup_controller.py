import random
from ..user.user_crud import UserCrud
from werkzeug.security import generate_password_hash


class SignupController:
    def __init__(self):
        self.user_crud = UserCrud()  # TODO inject this dependency

    def signup(self, full_name, email, password, password2):
        existing_email = self.user_crud.retrieve_by_email(email)
        if existing_email:
            return {"success": False, "message": "Email já cadastrado"}

        if len(password) < 8:
            return {"success": False, "message": "Senha deve ter no mínimo 8 caracteres"}

        if password2 != password:
            return {"success": False, "message": "Senhas não conferem"}

        password_hash = generate_password_hash(password)
        new_user = self.user_crud.create(full_name, email, password_hash)
        return {"success": True, "message": None, "user": new_user}


