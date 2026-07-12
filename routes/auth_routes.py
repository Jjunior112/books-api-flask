from flask import (
    Blueprint,
    request
)

from auth.auth_service import AuthService

from schemas import (
    LoginRequest
)

from schemas.auth_schema import LoginResponse
from schemas.mapper import user_to_response

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    get_jwt
)


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

    tokens = service.login(
        data.email,
        data.password
    )

    response = LoginResponse(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"]
    )

    return response.model_dump()

@auth_bp.post("/refresh")
@jwt_required(refresh=True)
def refresh():

    identity = get_jwt_identity()

    claims = get_jwt()

    access_token = create_access_token(
        identity=identity,
        additional_claims={
            "name": claims.get("name"),
            "email": claims.get("email")
        }
    )

    return {
        "access_token": access_token
    }