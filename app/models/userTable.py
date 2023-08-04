from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, "scrypt")
    
    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
        return data
    
    def __repr__(self):
        return "<User %r %r %r %r>" % self.id, self.name, self.email, self.password