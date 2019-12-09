from src.app import db


class Books(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Books id={}, title={}, author={}>".format(
            self.id, self.title, self.author
        )


class Requests(db.Model):
    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<User id={}, email={}>, book={}".format(
            self.id, self.email, self.book.id
        )

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.id,
            "email": self.email,
            "book_id": self.book_id,
            "timestamp": self.created_on,
        }
