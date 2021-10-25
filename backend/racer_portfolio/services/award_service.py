from racer_portfolio.models.award import *

def get_awards(user_id):
    return Award.query.filter_by(user_id=user_id).all()

def get_award(id):
    return Award.query.filter_by(id=id).one_or_none()

def add_award(user_id, title, detail):
    new_award = Award(user_id, title, detail)
    db.session.add(new_award)
    db.session.commit()
    return new_award.id

def edit_award(id, title, detail):
    award = Award.query.filter_by(id=id).one_or_none()
    award.title = title
    award.detail = detail
    db.session.add(award)
    db.session.commit()

def delete_award(id):
    award = Award.query.filter_by(id=id).one_or_none()
    db.session.delete(award)
    db.session.commit()