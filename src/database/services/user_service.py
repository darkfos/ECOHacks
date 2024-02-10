# Локальные директивы
from ..db import Database
from src.data_cls import UserInfo

# Внешние директивы
import logging


db = Database()


async def get_all_users() -> tuple | bool:
    """
    Асинхронный метод для получения всех пользователей
    """

    logging.info(msg="Осуществлён запрос на получение всех пользователей")

    with db.connect_to_db.cursor() as cursor:
        all_data: tuple = cursor.execute("SELECT * FROM Users")

        if all_data:
            return cursor.fetchall()
        else:
            return False


async def post_user(info_user: UserInfo) -> bool | str:
    """
    Асинхронный метод для создания пользователя
    """

    logging.info(msg="Осуществлён запрос на добавление пользователя")
    with db.connect_to_db.cursor() as cursor:
        try:

            tg_id: int = info_user.tg_id

            #Проверка на то, что User уже есть.
            cursor.execute("SELECT user_id FROM Users WHERE tg_id = (%s)", (tg_id, ))

            if cursor:
                return "Вы уже зарегистрированы!"

            data_to_add: tuple = info_user.name_user, info_user.tg_id, info_user.date_reg
            cursor.execute("INSERT INTO Users (name_user, tg_id, date_reg) VALUES (%s, %s, %s)", data_to_add)

            # Сохраняем изменения
            db.connect_to_db.commit()

            return True
        except Exception as ex:
            logging.critical(msg="Запрос на добавление пользователя не удался")
            return False


async def del_user(tg_id_user: int) -> bool:
    """
    Асинхронный метод для удаления пользователя по id
    """

    logging.info(msg="Осуществлён хапрос на удаления пользователя по id = {0}".format(tg_id_user))

    with db.connect_to_db.cursor() as cursor:

        try:
            cursor.execute("DELETE FROM Users WHERE tg_id = (%s)", (tg_id_user,))

            #Сохраняем изменения
            db.connect_to_db.commit()
            return True

        except Exception as ex:
            logging.critical(msg="Запрос на удаление пользователя по id = {0} не удался".format(tg_id_user))
            return False


async def del_all_users() -> bool:
    """
    Асинхронная функция, которая удаляет все поля в таблице
    """

    logging.info(msg="Запрос на удаление всех пользователей")

    try:
        with db.connect_to_db.cursor() as cursor:
            cursor.execute("DELETE FROM Users")

            #Сохраняем изменения
            db.connect_to_db.commit()

            return True

    except Exception as ex:
        logging.critical(msg="Запрос на удаление всех пользователей не удался")

        return False


async def update_user_name(user_name: str, tg_id: int) -> bool:
    """
    Асинхронный метод для изменения имени пользователя по tg ключу
    """

    logging.info(msg="Запрос на обновление имени пользователя по tg_id")

    try:
        with db.connect_to_db.cursor() as cursor:
            cursor.execute("UPDATE Users SET name_user = %s WHERE tg_id = (%s)", (user_name, tg_id))

            #Сохраняем изменения
            db.connect_to_db.commit()

            return True

    except Exception as ex:
        logging.critical(msg="Запрос на изменение имени пользователя не удался")

        return False