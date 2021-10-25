from racer_portfolio import db

class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(2048), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(),nullable=False)

    def __init__(self, user_id, title, detail, start_date, end_date):
        self.user_id = user_id
        self.title = title
        self.detail = detail
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "detail": self.detail,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
        }