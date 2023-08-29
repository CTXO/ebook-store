from .login_controller import LoginController
from .signup_controller import SignupController


class Facade:
    def signup(self, full_name, email, password, password2):
        return SignupController().signup(full_name, email, password, password2)

    def login(self, email, password):
        return LoginController().login(email,password)
