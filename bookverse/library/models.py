from ..app import db

ebook_library = db.Table('ebook_library',
                         db.Column('ebook_id', db.Integer, db.ForeignKey('ebook.id')),
                         db.Column('user_library_id', db.Integer, db.ForeignKey('user_library.id')),
                         )


class UserLibrary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ebooks = db.relationship('Ebook', backref='libraries', secondary=ebook_library)

    def __init__(self, user_id):
        self.user_id = user_id
