from flask import Blueprint, request

from schemas import UserRequest
from schemas.mapper import user_to_response

from services.user_service import UserService


user_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)

service = UserService()


@user_bp.post("")
def create():

    data = UserRequest(**request.get_json())

    user = service.create(
        data.model_dump()
    )

    response = user_to_response(user)

    return response.model_dump(), 201