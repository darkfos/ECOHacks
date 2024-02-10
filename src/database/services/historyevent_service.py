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
        all_data: tuple | str = cursor.execute("SELECT * FROM HistoryEvents")

        if all_data:
            return cursor.fetchall()
        else:
            logging.info(msg="Не удалось получить все запись историй")
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

            user_id = cursor.execute("SELECT user_id FROM Users WHERE tg_id = (%s)", (tg_key, )).fetchone()
            event_id = cursor.execute("SELECT event_id FROM Events WHERE tg_id = (%s)", (tg_key, )).fetchone()
            print(user_id, event_id)

            if user_id and event_id:
                all_data_to_add: tuple = history_data.message_history, history_data.date_message, user_id[0], event_id[0]
                cursor.execute("INSERT INFO HistoryEvent (message_history, date_message, user_id, event_id) VALUES (%s, %s, %s, %s)", all_data_to_add)

                #Сохраняем данные
                db.connect_to_db.commit()
                return True

            else:
                logging.info(msg="Не удалось создать историю")
                return False

    except Exception as ex:
        logging.info(msg="Не удалось получить добавить запись истории")
        return False


async def del_history(tg_id: int) -> bool:
    """
    Асинхронный метод для удаления истории по ключу
    """

    logging.info(msg="Отправлен запрос на удаление истории")

    try:
        with db.connect_to_db.cursor() as cursor:
            cursor.execute("DELETE FROM HistoryEvent WHERE tg_id = (%s)", (tg_id, ))

            #Сохраняем состояние таблицы
            db.connect_to_db.commit()

        return True

    except Exception as ex:
        logging.exception(msg="Не удалось удалить историю по id = {}".format(tg_id))
        return False