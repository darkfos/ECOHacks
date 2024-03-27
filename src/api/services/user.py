from src.api.schemas.users import User, UserAdd
from src.database.services.user_service import get_all_users, post_user
import logging

async def service_user_add(new_user: UserAdd):
    """
    Добавление нового пользователя
    """

    try:
        await post_user(info_user=new_user)
        return True
    except Exception as ex:
        return False


async def service_all_users() -> list[User] | bool:
    """
    Получение всех пользователей
    """

    try:
        all_user = await get_all_users()

        if all_user:
            response_lst: list = [User(user_id=user[0], name_user=user[1], tg_id=user[2], date_reg=user[3])
                                        for user in all_user]
            return response_lst

        return False

    except Exception as ex:
        logging.info(msg="Не удалось добавить пользователя")
        return False