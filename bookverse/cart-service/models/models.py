from ..app import db


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    pages = db.Column(db.Integer)
    authors = db.Column(db.String(255))
    year_of_release = db.Column(db.Integer)
    file_path = db.Column(db.String(255))
    cover_path = db.Column(db.String(255))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    price_cents = db.Column(db.Integer)

    def __init__(self, title=None, pages=None, authors=None, year_of_release=None, file_path=None, cover_path=None, cart_id=None):
        self.title = title
        self.pages = pages
        self.authors = authors
        self.year_of_release = year_of_release
        self.file_path = file_path
        self.cover_path = cover_path
        self.cart_id = cart_id


ebook_cart = db.Table('ebook_cart',
                      db.Column('ebook_id', db.Integer, db.ForeignKey('ebook.id')),
                      db.Column('cart_id', db.Integer, db.ForeignKey('cart.id')),
                      )


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,)  # db.ForeignKey('user.id')
    ebooks = db.relationship('Ebook', backref='carts', secondary=ebook_cart)

    def __init__(self, user_id):
        self.user_id = user_id

