from racer_portfolio import db

class License(db.Model):
    __tablename__ = "license"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    organization = db.Column(db.String(20), nullable=False)
    acquisition = db.Column(db.DateTime(),nullable=False)

    def __init__(self, user_id, title, organization, acquisition):
        self.user_id = user_id
        self.title = title
        self.organization = organization
        self.acquisition = acquisition
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "organization": self.organization,
            "acquisition": self.acquisition.strftime("%Y-%m-%d"),
        }