from racer_portfolio.models.project import *

def get_projects(user_id):
    return Project.query.filter_by(user_id=user_id).all()

def get_project(id):
    return Project.query.filter_by(id=id).one_or_none()

def add_project(user_id, title, detail, start_date, end_date):
    new_project = Project(user_id, title, detail, start_date, end_date)
    db.session.add(new_project)
    db.session.commit()
    return new_project.id

def edit_project(id, title, detail, start_date, end_date):
    project = Project.query.filter_by(id=id).one_or_none()
    project.title = title
    project.detail = detail
    project.start_date = start_date
    project.end_date = end_date
    db.session.add(project)
    db.session.commit()

def delete_project(id):
    project = Project.query.filter_by(id=id).one_or_none()
    db.session.delete(project)
    db.session.commit()