from fastapi import APIRouter
from src.api.schemas.users import User, UserAdd
from src.api.services.user import service_user_add, service_all_users

user_router: APIRouter = APIRouter(prefix="/users", tags=["User"])


@user_router.get("/")
async def get_all_users() -> list[User] | dict:
    """
        API request для получения всех пользователей
    """
    try:
        req = await service_all_users()

        if req:
            return req
        else:
            raise ValueError("Ошибка получения пользователей")

    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.post("/add")
async def get_new_user(new_user: UserAdd) -> dict:
    """
        API request для добавления пользователя
    """

    try:
        req = await service_user_add(new_user=new_user)
        return {
            "message": "success"
        }
    except Exception as ex:
        return {
            "message": "Error"
        }