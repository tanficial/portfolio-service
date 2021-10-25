from racer_portfolio.models.user import *

def get_user_by_email(email):
    return User.query.filter_by(email=email).one_or_none()

def get_user_by_id(id):
    return User.query.filter_by(id=id).one_or_none()

def get_users(name):
    return User.query.filter(User.name.like(f"%{name}%")).all()

def add_user(email, password, name):
    new_user = User(email, password, name)
    db.session.add(new_user)
    db.session.commit()

def change_image(id, image_url):
    user = get_user_by_id(id)
    user.image = image_url
    db.session.add(user)
    db.session.commit()

def update_user(id, name, description):
    user = get_user_by_id(id)
    user.name = name
    user.description = description
    db.session.add(user)
    db.session.commit()