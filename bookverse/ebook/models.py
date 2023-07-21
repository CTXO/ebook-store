from ..app import db

class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    pages = db.Column(db.Integer)
    authors = db.Column(db.String(255))
    year_of_release = db.Column(db.Integer)
    file_path = db.Column(db.String(255))
    cover_path = db.Column(db.String(255))


