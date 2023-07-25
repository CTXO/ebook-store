from .models import Cart
from .repo_interface import ICartRepo
from ..app import db
from ..ebook.models import Ebook


class CartRepoSqlLite(ICartRepo):
    def create_cart(self, user_id):
        cart = Cart(user_id)
        db.session.add(cart)
        db.session.commit()
        return cart

    def list_ebooks(self, user_id):
        cart = Cart.query.filter_by(user_id=user_id).first()
        if not cart:
            raise Exception('Cart not found')
        return cart.ebooks

    def add_to_cart(self, user_id, ebook_id):
        cart = Cart.query.filter_by(user_id=user_id).first()
        print("cart is", cart)
        if not cart:
            raise Exception('Cart not found')
        # check if ebook is already on cart
        if Cart.query.filter(Cart.ebooks.any(id=ebook_id) & Cart.user_id == user_id).first():
            return cart
        ebook = Ebook.query.filter_by(id=ebook_id).first()
        cart.ebooks.append(ebook)
        db.session.commit()
        return cart
