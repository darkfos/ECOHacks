from src.api import UserSchema, UserSchemaUpdate
from src.api import UserModel
from src import get_users_by_tgid, get_user_by_idp, del_user_by_idp, del_user, post_user, update_user_name


async def create_user(data: UserSchema) -> UserModel:
    """
    Создаём пользователя по схеме
    """
    user: UserModel = UserModel(name_user=data.name_user, tg_id=data.tg_id, date_reg=data.date_reg)

    #Заносим данные в таблицу Users
    response = post_user(info_user=user)
    return response


async def get_user_idp(idp: int) -> UserModel:
    """
    Получаем пользователя по первичному ключу
    """

    response = await get_user_by_idp(idp)
    return response


async def get_user_tgid(tg_id: int) -> UserModel:
    """
    Получаем пользователя по tg_id
    """

    response = await get_users_by_tgid(tg_id=tg_id)
    return response


async def del_user_tgid(tg_id: int) -> dict:
    """
    Удаляем пользователя по tg_id
    """

    response = await del_user_tgid(tg_id=tg_id)

    if response: return {"response": True}
    return {"response": False}


async def del_user_id(id: int) -> dict:
    """
    Удаляем пользователя по id
    """

    response = await del_user_tgid(id=id)

    if response: return {"response": True}
    return {"response": False}


async def update_user(data: UserSchemaUpdate) -> UserModel:
    """
    Обновляем информацию о user
    """

    user: UserModel = UserModel(name_user=data.name_user, tg_id=data.tg_id, date_reg=data.date_reg)

    #Заносим данные в таблицу Users
    response = post_user(info_user=user)
    return response