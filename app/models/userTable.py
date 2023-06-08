from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
        return data
    
    def __repr__(self):
        return "<User %r %r %r>" % self.id, self.name, self.email