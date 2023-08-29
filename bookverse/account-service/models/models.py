from ..app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name, email, password_hash):
        self.name = name
        self.password_hash = password_hash
        self.email = email
