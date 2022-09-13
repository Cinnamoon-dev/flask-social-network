from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username
        # use o %r pois é uma string pura, ou seja não serão executados comandos especiais como \n eles serao printados


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.Text)

    user = db.relationship('User', foreign_keys=id_user)
    # one to one

    def __init__(self, content, user_id):
        self.content = content
        self.id_user = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    id_follower = db.Column(db.Integer, db.ForeginKey('users.id'))

    user = db.relationship('User', foreign_keys=id_user)
    follower = db.relationship('User', foreign_keys=id_follower)
