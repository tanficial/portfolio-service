from flask import Blueprint, request, session
from flask_restful import Resource, Api

from racer_portfolio.utils.auth import login_required
from racer_portfolio.services.user_service import get_user_by_id
from racer_portfolio.services.education_service import get_educations, get_education, add_education, edit_education, delete_education

bp = Blueprint('education', __name__)

class Education(Resource):
    @login_required
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404
        
        result = []
        educations = get_educations(user_id)
        for education in educations:
            result.append(education.to_dict())
        return {"result":"success", "educations": result}, 200

    @login_required
    def post(self, user_id):
        if user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403

        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404
        
        school = request.form.get("school")
        major = request.form.get("major")
        degree = request.form.get("degree")
        if request.json:
            school = request.json.get("school")
            major = request.json.get("major")
            degree = request.json.get("degree")
        new_item_id = add_education(user_id, school, major, degree)
        return {"result": "success", "itemId": new_item_id}, 201
    
    @login_required
    def patch(self, education_id):
        education = get_education(education_id)
        if education is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if education.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        school = request.form.get("school")
        major = request.form.get("major")
        degree = request.form.get("degree")
        if request.json:
            school = request.json.get("school")
            major = request.json.get("major")
            degree = request.json.get("degree")
        edit_education(education_id, school, major, degree)
        return {"result": "success"}, 200

    @login_required
    def delete(self, education_id):
        education = get_education(education_id)
        if education is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if education.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        delete_education(education_id)
        return {"result": "success"}, 204

api = Api(bp)

api.add_resource(Education, "/user/<int:user_id>", "/<int:education_id>")