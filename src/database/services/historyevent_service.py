# Локальные директивы
from ..db import Database
from src.data_cls import HistoryEventInfo

# Внешние директивы
import logging


db = Database()


async def get_all_histories() -> tuple | bool:
    """
    Асинхронный метод для получения всех историй событий
    """

    logging.info(msg="Пользователь отправил запрос на получение всех историй")

    with db.connect_to_db.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM HistoryEvents")
            all_data: tuple = cursor.fetchall()
            if all_data:
                return all_data
            else:
                logging.info(msg="Не удалось получить все записи историй")
                return False
        except Exception as ex:
            logging.error(msg=f"Ошибка при получении всех записей историй: {ex}")
            return False


async def get_history_by_id(tg_id: int) -> tuple | bool:
    """
    Асинхронный метод для получения события по ключу телеграмма
    """

    logging.info(msg="Пользователь отправил запрос на получение истории")
    with db.connect_to_db.cursor() as cursor:
        data: tuple | str = cursor.execute("SELECT * FROM HistoryEvents WHERE tg_id = (%s)", (tg_id, ))

        if data:
            return cursor.fetchall()
        else:
            logging.info(msg="Не удалось получить все записи историй по tg_id")
            return False


async def post_history(history_data: HistoryEventInfo):
    """
    Асинхронный метод на добавление истории
    """

    logging.info(msg="Пользователь отправил запрос на создание истории")
    try:
        with db.connect_to_db.cursor() as cursor:

            #Делаем запрос на получение ключей
            tg_key: int = history_data.tg_id

            cursor.execute("SELECT user_id FROM Users WHERE tg_id = (%s)", (tg_key, ))
            user_id: int = cursor.fetchone()[0]
            cursor.execute("SELECT event_id FROM Events WHERE tg_id = (%s)", (tg_key, ))
            event_id: int = cursor.fetchone()[0]

            all_data_to_add: tuple = history_data.message_history, history_data.date_message, user_id, event_id
            cursor.execute("INSERT INTO HistoryEvents (message_history, date_message, user_id, event_id) VALUES (%s, %s, %s, %s)", all_data_to_add)

            #Сохраняем данные
            db.connect_to_db.commit()
            return True

    except Exception as ex:
        logging.info(msg="Не удалось получить добавить запись истории")
        return False


async def del_history(tg_id: int) -> bool:
    """
    Асинхронный метод для удаления истории по ключу
    """

    logging.info(msg="Отправлен запрос на удаление истории")

    with db.connect_to_db.cursor() as cursor:
        try:
            cursor.execute("SELECT user_id FROM Users WHERE tg_id = (%s)", (tg_id, ))

            user_id: list = cursor.fetchone()

            if user_id is not None:
                cursor.execute("DELETE FROM HistoryEvents WHERE user_id = (%s)", (user_id[0], ))

                #Сохраняем состояние таблицы
                db.connect_to_db.commit()

                return True

        except Exception as ex:
            logging.exception(msg="Не удалось удалить историю по id = {}".format(tg_id))
            return False