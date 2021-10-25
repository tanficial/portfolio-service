from flask import Blueprint, jsonify, request, session

from racer_portfolio.utils.auth import login_required
from racer_portfolio.utils.validation import validate_name
from racer_portfolio.services.user_service import get_user_by_id, get_users, update_user, change_image

bp = Blueprint('user', __name__)

@bp.route("/", methods=["GET"])
@login_required
def users():
    query = request.args.get("query")
    result = []

    users = get_users(query)
    for user in users:
        result.append(user.to_dict())
    
    return jsonify(result="success", users=result), 200

@bp.route("/<int:user_id>", methods=["GET"])
@login_required
def user_info(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return jsonify(result="failed", message="존재하지 않는 사용자입니다."), 404

    return jsonify(result="success", user=user.to_dict()), 200

@bp.route("/<int:user_id>", methods=["PATCH"])
@login_required
def user_info_update(user_id):
    if user_id != session.get("auth"):
        return jsonify(result="falied", message="권한이 없는 사용자입니다."), 403

    user = get_user_by_id(user_id)
    if user is None:
        return jsonify(result="failed", message="존재하지 않는 사용자입니다."), 404

    name = request.form.get("name")
    description = request.form.get("description")
    if request.json:
        name = request.json.get("name")
        description = request.json.get("description")
    
    if validate_name(name) == False:
        return jsonify(result="faile", message="이름은 영문이나 한글로 입력해주세요."), 400

    update_user(user_id, name, description)
    return jsonify(result="success"), 200

@bp.route("/<int:user_id>/image", methods=["PATCH"])
@login_required
def edit_image(user_id):
    if user_id != session.get("auth"):
        return jsonify(result="falied", message="권한이 없는 사용자입니다."), 403

    user = get_user_by_id(user_id)
    if user is None:
        return jsonify(result="failed", message="존재하지 않는 사용자입니다."), 404

    image = request.form.get("image")
    if request.json:
        image = request.json.get("image")
    change_image(user_id, image)
    return jsonify(result="success"), 200
