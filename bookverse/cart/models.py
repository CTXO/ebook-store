from ..app import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ebooks = db.relationship('Ebook', backref='cart')

    def __init__(self, user_id):
        self.user_id = user_id


