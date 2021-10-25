from racer_portfolio import db

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "description": self.description,
            "image": self.image,
        }