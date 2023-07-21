from .buy_book import buy_books


class Facade:
    @staticmethod
    def checkout():
        return buy_books()

    def payment_succeeded(self):
        pass

