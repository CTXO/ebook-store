from .signup_controller import SignupController


class Facade:
    def signup(self, full_name, email, password, password2):
        return SignupController().signup(full_name, email, password, password2)

