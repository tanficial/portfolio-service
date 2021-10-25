from flask import Blueprint, jsonify

from racer_portfolio.utils.auth import login_required
from racer_portfolio.services.award_service import get_awards
from racer_portfolio.services.education_service import get_educations
from racer_portfolio.services.license_service import get_licenses
from racer_portfolio.services.project_service import get_projects
from racer_portfolio.services.user_service import get_user_by_id

bp = Blueprint('portfolio', __name__)

@bp.route("/<int:user_id>", methods=["GET"])
@login_required
def get_portfolio(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        return jsonify(result="falied", message="존재하지 않는 사용자입니다."), 404
    result = {
        "user": user.to_dict(),
        "awards": [],
        "educations": [],
        "licenses": [],
        "projects": [],
    }

    awards = get_awards(user_id)
    educations = get_educations(user_id)
    licenses = get_licenses(user_id)
    projects = get_projects(user_id)

    for award in awards:
        result["awards"].append(award.to_dict())
    for education in educations:
        result["educations"].append(education.to_dict())
    for _license in licenses:
        result["licenses"].append(_license.to_dict())
    for project in projects:
        result["projects"].append(project.to_dict())

    return jsonify(result="success", portfolio=result), 200
