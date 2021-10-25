from datetime import datetime

from flask import Blueprint, request, session
from flask_restful import Resource, Api

from racer_portfolio.utils.auth import login_required
from racer_portfolio.services.user_service import get_user_by_id
from racer_portfolio.services.license_service import get_licenses, get_license, add_license, edit_license, delete_license

bp = Blueprint('license', __name__)

class License(Resource):
    @login_required
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404
        
        result = []

        licenses = get_licenses(user_id)
        for _license in licenses:
            result.append(_license.to_dict())
        return {"result":"success", "licenses": result}, 200

    @login_required
    def post(self, user_id):
        if user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403

        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404

        title = request.form.get("title")
        organization = request.form.get("organization")
        acquisition = request.form.get("acquisition")
        if request.json:
            title = request.json.get("title")
            organization = request.json.get("organization")
            acquisition = request.json.get("acquisition")

        if title and organization and acquisition:
            try:
                acquisition = datetime.strptime(acquisition, "%Y-%m-%d")
            except ValueError:
                return {"result": "failed", "message": "올바른 날짜 형식이 아닙니다."}, 400
            if acquisition > datetime.now():
                return {"result": "failed", "message": "현재 날짜보다 앞선 날짜를 선택해주세요."}, 400

            new_item_id = add_license(user_id, title, organization, acquisition)
            return {"result": "success", "itemId": new_item_id}, 201
        else:
            return {"result": "failed", "message": "모든 정보를 입력해주세요."}, 400
    @login_required
    def patch(self, license_id):
        _license = get_license(license_id)
        if _license is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if _license.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403

        title = request.form.get("title")
        organization = request.form.get("organization")
        acquisition = request.form.get("acquisition")
        if request.json:
            title = request.json.get("title")
            organization = request.json.get("organization")
            acquisition = request.json.get("acquisition")
            
        if title and organization and acquisition:
            try:
                acquisition = datetime.strptime(acquisition, "%Y-%m-%d")
            except ValueError:
                return {"result": "failed", "message": "올바른 날짜 형식이 아닙니다."}, 400
            if acquisition > datetime.now():
                return {"result": "failed", "message": "현재 날짜보다 앞선 날짜를 선택해주세요."}, 400

            edit_license(license_id, title, organization, acquisition)
            return {"result": "success"}, 200
        else:
            return {"result": "failed", "message": "모든 정보를 입력해주세요."}, 400

    @login_required
    def delete(self, license_id):
        _license = get_license(license_id)
        if _license is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if _license.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        delete_license(license_id)
        return {"result": "success"}, 204

api = Api(bp)

api.add_resource(License, "/user/<int:user_id>", "/<int:license_id>")