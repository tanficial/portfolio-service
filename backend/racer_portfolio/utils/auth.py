from functools import wraps

from flask import session

def login_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        logined_user_id = session.get("auth")
        if logined_user_id is None:
            return {"result": "falied", "message": "로그인이 필요합니다."}, 401
        return func(*args, **kwargs)
    return decorator
