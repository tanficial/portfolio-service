from racer_portfolio.models.license import *

def get_licenses(user_id):
    return License.query.filter_by(user_id=user_id).all()

def get_license(id):
    return License.query.filter_by(id=id).one_or_none()

def add_license(user_id, title, organization, acquisition):
    new_license = License(user_id, title, organization, acquisition)
    db.session.add(new_license)
    db.session.commit()
    return new_license.id

def edit_license(id, title, organization, acquisition):
    _license = License.query.filter_by(id=id).one_or_none()
    _license.title = title
    _license.organization = organization
    _license.acquisition = acquisition
    db.session.add(_license)
    db.session.commit()

def delete_license(id):
    _license = License.query.filter_by(id=id).one_or_none()
    db.session.delete(_license)
    db.session.commit()