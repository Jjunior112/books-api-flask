from flask import (
    Blueprint,
    request
)

from auth.auth_service import AuthService

from schemas import (
    LoginRequest
)

from schemas.mapper import user_to_response


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

service = AuthService()


@auth_bp.post("/login")
def login():

    data = LoginRequest(
        **request.get_json()
    )

    user = service.login(
        data.email,
        data.password
    )

    response = user_to_response(
        user
    )

    return response.model_dump()