from .repo_interface import ICartRepo
from ..app import db

from .models import Cart


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
    
