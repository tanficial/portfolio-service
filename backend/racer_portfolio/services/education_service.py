from racer_portfolio.models.education import *

def get_educations(user_id):
    return Education.query.filter_by(user_id=user_id).all()

def get_education(id):
    return Education.query.filter_by(id=id).one_or_none()

def add_education(user_id, school, major, degree):
    new_education = Education(user_id, school, major, degree)
    db.session.add(new_education)
    db.session.commit()
    return new_education.id

def edit_education(id, school, major, degree):
    education = Education.query.filter_by(id=id).one_or_none()
    education.school = school
    education.major = major
    education.degree = degree
    db.session.add(education)
    db.session.commit()

def delete_education(id):
    education = Education.query.filter_by(id=id).one_or_none()
    db.session.delete(education)
    db.session.commit()