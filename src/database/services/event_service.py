# Локальные директивы
from ..db import Database
from src.data_cls import EventInfo

# Внешние директивы
import logging


db = Database()


class EventServiceDB:
    @staticmethod
    async def get_all_events() -> list | bool:
        """
        Асинхронный метод на получение всех событий
        """

        logging.info(msg="Отправлен запрос на получение всех событий")

        with db.connect_to_db.cursor() as cursor:

            try:
                cursor.execute("SELECT * FROM events")
                all_data: tuple = cursor.fetchall()
                if all_data:
                    return all_data
                else:
                    return False

            except Exception as ex:
                logging.info(msg="События не были найдены")
                return False

    @staticmethod
    async def get_event_by_id(tg_id: int) -> list | bool:
        """
        Асинхронный метод на получение события по tg_id
        """

        logging.info(msg="Отправлен запрос на получение события по ключу")

        with db.connect_to_db.cursor() as cursor:
            cursor.execute("SELECT * FROM Events WHERE tg_id = (%s)", (tg_id, ))

            all_data: tuple | str = cursor.fetchall()

            if all_data:
                return all_data
            else:
                logging.info(msg="Событие не было найдено")
                return False

    @staticmethod
    async def get_event_by_idp(id: int) -> list | bool:
        """
        Асинхронный метод на получение события по id, первичному ключу
        """

        logging.info(msg="Отправлен запрос на получение обытия по первичному ключу")

        with db.connect_to_db.cursor() as cursor:
            cursor.execute("SELECT * FROM Events WHERE event_id = (%s)", (id, ))

            all_data: list = cursor.fetchall()

            if all_data: return all_data
            return False

    @staticmethod
    async def post_event(event_data: EventInfo) -> bool:
        """
        Асинхронный метод для добавления события
        """

        logging.info(msg="Отправлен запрос на создание события")

        try:
            all_data: tuple = event_data.tg_id, event_data.message_event, event_data.date_event, event_data.photo

            #Получаем user id, по tg_id

            with db.connect_to_db.cursor() as cursor:
                cursor.execute("SELECT user_id FROM Users WHERE tg_id = (%s)", (event_data.tg_id, ))
                user_id: tuple = cursor.fetchone()

                if user_id:
                    user_id: int = user_id[0]

                    cursor.execute("INSERT INTO Events (tg_id, message_event, date_event, photo, user_id) VALUES (%s, %s, %s, %s, %s)", (*all_data, user_id, ))

                    db.connect_to_db.commit()
                else: raise Exception
            return True
        except Exception as ex:
            logging.exception(msg="Не удалось создать событие")
            return False

    @staticmethod
    async def del_events(tg_id: int) -> bool:
        """
        Асинхронный метод для удаления записей по tg_id
        """

        logging.info(msg="Отправлен запрос на удаления события")

        try:
            with db.connect_to_db.cursor() as cursor:
                cursor.execute("DELETE FROM Events WHERE tg_id = (%s)", (tg_id, ))

                db.connect_to_db.commit()
                return True

        except Exception as ex:
            logging.critical(msg="Не удалось удалить событие")
            return False

    @staticmethod
    async def del_events_by_idp(id: int) -> bool:
        """
        Асинхронный метод для удаления записей по id, Первичному ключу
        """

        logging.info(msg="Отправлен запрос на удаления события по id")

        with db.connect_to_db.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM Events WHERE event_id = (%s)", (id, ))
                return True
            except Exception as ex:
                logging.critical(msg="Ну удалось удалить событие по первичному ключу")
            return False