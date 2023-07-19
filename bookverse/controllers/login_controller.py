from user.user_crud import UserCrud


class LoginController:
    user_crud = UserCrud()  # TODO inject

    def login(self, email, password):
        pass


