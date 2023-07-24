from ..app import db

ebook_cart = db.Table('ebook_cart',
                      db.Column('ebook_id', db.Integer, db.ForeignKey('ebook.id')),
                      db.Column('cart_id', db.Integer, db.ForeignKey('cart.id')),
                      )


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ebooks = db.relationship('Ebook', backref='carts', secondary=ebook_cart)

    def __init__(self, user_id):
        self.user_id = user_id
