from werkzeug.security import generate_password_hash

from bookverse.user.models import User
from bookverse.user.user_crud import UserCrud


class LoginController:
    pass


class SignupController:
    user_crud = UserCrud()  # TODO inject this dependency

    def signup(self, name, username, email, password):
        print("email is", email)
        existing_user = User.query.filter(User.username == username).first()
        if existing_user:
            return {"success": False, "message": "Nome de usuário já cadastrado"}

        existing_email = User.query.filter(User.email == email).first()
        print("existing email is", existing_email)
        if existing_email:
            return {"success": False, "message": "Email já cadastrado"}

        if len(password) < 8:
            return {"success": False, "message": "Senha deve ter no mínimo 8 caracteres"}

        password_hash = generate_password_hash(password)
        new_user = self.user_crud.create(name, username, email, password_hash)
        return {"success": True, "message": None, "user": new_user}


