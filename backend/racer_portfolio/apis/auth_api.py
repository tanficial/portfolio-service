from flask import Blueprint, jsonify, request, session
from flask_bcrypt import Bcrypt

from racer_portfolio.utils.auth import login_required
from racer_portfolio.utils.validation import validate_email, validate_password, validate_name
from racer_portfolio.services.user_service import get_user_by_email, add_user

bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@bp.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if request.json:
        email = request.json.get("email")
        password = request.json.get("password")

    user = get_user_by_email(email)
    if user is None:
        return jsonify(result="failed", message="이메일 혹은 비밀번호가 일치하지 않습니다."), 401
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify(result="failed", message="이메일 혹은 비밀번호가 일치하지 않습니다."), 401
    
    session["auth"] = user.id
    return jsonify(result="success", message="login success", user=user.to_dict()), 200

@bp.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    name = request.form.get("name")
    if request.json:
        email = request.json.get("email")
        password = request.json.get("password")
        name = request.json.get("name")

    if not validate_email(email):
        return jsonify(result="failed", message="올바른 이메일 형식이 아닙니다."), 400

    if not validate_password(password):
        return jsonify(result="failed", message="올바른 비밀번호가 아닙니다."), 400
    
    if not validate_name(name):
        return jsonify(result="failed", message="올바른 이름이 아닙니다."), 400

    user = get_user_by_email(email)
    if user is not None:
        return jsonify(result="failed", message="이미 존재하는 이메일입니다."), 400

    pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    add_user(email, pw_hash, name)
    return jsonify(result="success", message="signup success"), 201

@bp.route("/logout")
@login_required
def logout():
    session.clear()
    return jsonify(result="success", message="logout success"), 200