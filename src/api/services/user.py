from src.api.schemas.users import User, UserAdd
from src.database.services.user_service import UserServiceDB
import logging


class UserServiceAPI:
    @staticmethod
    async def service_user_add(new_user: UserAdd):
        """
        Добавление нового пользователя
        """

        try:
            await UserServiceDB.post_user(info_user=new_user)
            return True
        except Exception as ex:
            return False

    @staticmethod
    async def service_all_users() -> list[User] | bool:
        """
        Получение всех пользователей
        """

        try:
            all_user = await UserServiceDB.get_all_users()

            if all_user:
                response_lst: list = [User(user_id=user[0], name_user=user[1], tg_id=user[2], date_reg=user[3])
                                            for user in all_user]
                return response_lst

            return False

        except Exception as ex:
            logging.exception(msg="Не удалось добавить пользователя")
            return False

    @staticmethod
    async def service_get_user_by_tgid(tg_id: int) -> User | bool:
        """
        Получение пользователя по tg_id
        """

        try:

            user = await UserServiceDB.get_users_by_tgid(tg_id=tg_id)
            print(user)
            if user:
                return User(user_id=user[0], name_user=user[1], tg_id=user[2], date_reg=user[3])
            return False

        except Exception as ex:
            logging.exception(msg="Не удалось получить пользователя по tg_id")

    @staticmethod
    async def service_get_user_by_id(id: int) -> User | bool:
        """
        Получение пользователя по id
        """

        try:

            user = await UserServiceDB.get_user_by_idp(id=id)
            if user:
                return User(user_id=user[0], name_user=user[1], tg_id=user[2], date_reg=user[3])
            return False

        except Exception as ex:
            logging.exception(msg="Не удалось получить пользователя по tg_id")

    @staticmethod
    async def service_del_user_by_tg_id(tg_id: int) -> bool:
        """
        Удаление пользователя по tg_id
        """

        try:
            to_del_user: bool = await UserServiceDB.del_user(tg_id_user=tg_id)

            if to_del_user:
                return True
            else:
                raise Exception("Ошибка")

        except Exception as ex:
            logging.exception(msg="Не удалось удалить пользователя")
            return False

    @staticmethod
    async def service_del_user_by_id(id: int) -> bool:
        """
        Удаление пользователя по id
        """

        try:
            to_del_user: bool = await UserServiceDB.del_user_by_idp(id=id)
            if to_del_user:
                return True
            else:
                raise Exception("Ошибка")
        except Exception as ex:
            logging.exception(msg="Не удалось удалить пользователя")
            return False

    @staticmethod
    async def service_upd_user_name(tg_id:int, user_name: str) -> User | bool:
        """
        Обновление имени User
        """

        try:
            upd_user = await UserServiceDB.update_user_name(user_name=user_name, tg_id=tg_id)
            if upd_user:
                return User(user_id=upd_user[0], name_user=upd_user[1], tg_id=upd_user[2], date_reg=upd_user[3])
            else:
                raise Exception("Ошибка")
        except Exception as ex:
            logging.exception(msg="Не удалось обновить имя пользователя")
            return False