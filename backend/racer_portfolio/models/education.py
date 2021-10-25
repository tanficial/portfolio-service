from racer_portfolio import db

class Education(db.Model):
    __tablename__ = "education"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    school = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(20), nullable=False)
    degree = db.Column(db.String(20), nullable=False)

    def __init__(self, user_id, school, major, degree):
        self.user_id = user_id
        self.school = school
        self.major = major
        self.degree = degree

    def to_dict(self):
        return {
            "id": self.id,
            "school": self.school,
            "major": self.major,
            "degree": self.degree,
        }