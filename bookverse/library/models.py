from ..app import db


class UserLibrary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ebooks = db.relationship('Ebook', backref='library')

    def __init__(self, user_id):
        self.user_id = user_id
