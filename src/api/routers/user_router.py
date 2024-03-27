import logging

from fastapi import APIRouter
from src.api.schemas.users import User, UserAdd
from src.api.services.user import UserServiceAPI

user_router: APIRouter = APIRouter(prefix="/users", tags=["User"])


@user_router.get("/")
async def get_all_users() -> list[User] | dict:
    """
        API request для получения всех пользователей
    """
    try:
        req = await UserServiceAPI.service_all_users()

        if req:
            return req
        else:
            raise ValueError("Ошибка получения пользователей")

    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.get("/by_tg_id")
async def get_user_by_tg_id(tg_id: int) -> User | dict:
    """
    Получение пользователя по tg_id
    """

    try:
        user: User = await UserServiceAPI.service_get_user_by_tgid(tg_id=tg_id)
        if user:
            return user
    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.get("/by_id")
async def get_user_by_tg_id(id: int) -> User | dict:
    """
    Получение пользователя по id
    """

    try:
        user: User = await UserServiceAPI.service_get_user_by_id(id=id)
        if user:
            return user
    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.post("/add")
async def add_new_user(new_user: UserAdd) -> dict:
    """
        API request для добавления пользователя
    """

    try:
        req = await UserServiceAPI.service_user_add(new_user=new_user)
        return {
            "message": "success"
        }
    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.delete("/del")
async def del_user(tg_id: int) -> dict:
    """
    Удаления пользователя по его tg_id
    """

    try:
        req = await UserServiceAPI.service_del_user_by_tg_id(tg_id=tg_id)
        if req:
            return {
                "message": "Success"
            }
        else:
            raise ValueError("Ошибка")
    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.delete("/del_by_id")
async def del_user_by_id(id: int) -> dict:
    """
    Удаление пользователя по его id
    """

    try:
        req = await UserServiceAPI.service_del_user_by_id(id=id)
        if req:
            return {
                "message": "Success"
            }
        else:
            raise ValueError("Ошибка")
    except Exception as ex:
        return {
            "message": "Error"
        }


@user_router.put("/update_user/{tg_id}/{new_name_user}")
async def update_user_name(tg_id: int, new_name_user: str) -> User | dict:
    """
    Обновление имение пользователя
    """

    try:
        req = await UserServiceAPI.service_upd_user_name(tg_id=tg_id, user_name=new_name_user)

        if req:
            return req
        else:
            raise ValueError("Ошибка")
    except Exception as ex:
        return {
            "message": "Error"
        }