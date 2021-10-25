from datetime import datetime

from flask import Blueprint, request, session
from flask_restful import Resource, Api

from racer_portfolio.utils.auth import login_required
from racer_portfolio.services.user_service import get_user_by_id
from racer_portfolio.services.project_service import get_projects, get_project, add_project, edit_project, delete_project

bp = Blueprint('project', __name__)

class Project(Resource):
    @login_required
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404
        
        result = []
        projects = get_projects(user_id)
        for project in projects:
            result.append(project.to_dict())
        return {"result":"success", "projects": result}, 200
    
    @login_required
    def post(self, user_id):
        if user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403

        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404

        title = request.form.get("title")
        detail = request.form.get("detail")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        if request.json:
            title = request.json.get("title")
            detail = request.json.get("detail")
            start_date = request.json.get("start_date")
            end_date = request.json.get("end_date")

        if title and detail and start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                return {"result": "failed", "message": "올바른 날짜 형식이 아닙니다."}, 400
            if start_date > end_date:
                return {"result": "failed", "message": "종료 날짜는 시작 날짜 다음이어야 합니다."}, 400
            if start_date > datetime.now() or end_date > datetime.now():
                return {"result": "failed", "message": "현재 날짜보다 앞선 날짜를 선택해주세요."}, 400

            new_item_id = add_project(user_id, title, detail, start_date, end_date)
            return {"result": "success", "itemId": new_item_id}, 201
        else:
            return {"result": "failed", "message": "모든 정보를 입력해주세요."}, 400

    @login_required
    def patch(self, project_id):
        project = get_project(project_id)
        if project is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if project.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        title = request.form.get("title")
        detail = request.form.get("detail")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        if request.json:
            title = request.json.get("title")
            detail = request.json.get("detail")
            start_date = request.json.get("start_date")
            end_date = request.json.get("end_date")
            
        if title and detail and start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                return {"result": "failed", "message": "올바른 날짜 형식이 아닙니다."}, 400
            if start_date > end_date:
                return {"result": "failed", "message": "종료 날짜는 시작 날짜 다음이어야 합니다."}, 400
            if start_date > datetime.now() or end_date > datetime.now():
                return {"result": "failed", "message": "현재 날짜보다 앞선 날짜를 선택해주세요."}, 400

            edit_project(project_id, title, detail, start_date, end_date)
            return {"result": "success"}, 200
        else:
            return {"result": "failed", "message": "모든 정보를 입력해주세요."}, 400

    @login_required
    def delete(self, project_id):
        project = get_project(project_id)
        if project is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if project.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        delete_project(project_id)
        return {"result": "success"}, 204

api = Api(bp)

api.add_resource(Project, "/user/<int:user_id>", "/<int:project_id>")