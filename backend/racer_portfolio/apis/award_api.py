from flask import Blueprint, request, session
from flask_restful import Resource, Api

from racer_portfolio.utils.auth import login_required
from racer_portfolio.services.user_service import get_user_by_id
from racer_portfolio.services.award_service import get_awards, get_award, add_award, edit_award, delete_award

bp = Blueprint('award', __name__)

class Award(Resource):
    @login_required
    def get(self, user_id):
        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404
        
        result = []
        awards = get_awards(user_id)
        for award in awards:
            result.append(award.to_dict())
        return {"result":"success", "awards": result}, 200

    @login_required
    def post(self, user_id):
        if user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403

        user = get_user_by_id(user_id)
        if user is None:
            return {"result": "failed", "message": "존재하지 않는 사용자입니다."}, 404
        
        title = request.form.get("title")
        detail = request.form.get("detail")
        if request.json:
            title = request.json.get("title")
            detail = request.json.get("detail")

        if title and detail:
            new_item_id = add_award(user_id, title, detail)
            return {"result": "success", "itemId": new_item_id}, 201
        else:
            return {"result": "failed", "message": "모든 정보를 입력해주세요."}, 400
    
    @login_required
    def patch(self, award_id):
        award = get_award(award_id)
        if award is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if award.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        title = request.form.get("title")
        detail = request.form.get("detail")
        if request.json:
            title = request.json.get("title")
            detail = request.json.get("detail")
        if title and detail:
            edit_award(award_id, title, detail)
            return {"result": "success"}, 200
        else:
            return {"result": "failed", "message": "모든 정보를 입력해주세요."}, 400

    @login_required
    def delete(self, award_id):
        award = get_award(award_id)
        if award is None:
            return {"result": "failed", "message": "존재하지 않는 리소스입니다."}, 404
        if award.user_id != session.get("auth"):
            return {"result": "failed", "message": "권한이 없는 사용자입니다."}, 403
        
        delete_award(award_id)        
        return {"result": "success"}, 204

api = Api(bp)

api.add_resource(Award, "/user/<int:user_id>", "/<int:award_id>")