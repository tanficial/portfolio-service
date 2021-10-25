from racer_portfolio import db

class Award(db.Model):
    __tablename__ = "award"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(2048), nullable=False)

    def __init__(self, user_id, title, detail):
        self.user_id = user_id
        self.title = title
        self.detail = detail
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "detail": self.detail,
        }