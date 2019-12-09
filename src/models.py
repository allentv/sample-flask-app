from src.app import db


class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    title_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __repr__(self):
        return "<User id={}, email={}>, title_id={}".format(
            self.id, self.email, self.title_id
        )


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return "<Books id={}, title={}, author={}>".format(
            self.id, self.title, self.author
        )
