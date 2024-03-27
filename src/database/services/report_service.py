# Локальные директивы
from ..db import Database
from src.data_cls import ReportInfo

# Внешние директивы
import logging


db = Database()


class ReportServiceDB:
    @staticmethod
    async def post_report(data_report: ReportInfo, flag: False) -> bool:
        """
        Асинхронный метод на добавление отчёта
        """

        with db.connect_to_db.cursor() as cursor:
            try:
                data_to_add: tuple = data_report.message_history, data_report.tg_id, data_report.street_data, data_report.latitude, data_report.longtitude, data_report.photo, data_report.date_report
                cursor.execute("INSERT INTO reports (message_history, tg_id, street_data, latitude, longitude, photo, date_report) VALUES (%s, %s, %s, %s, %s, %s, %s)", (*data_to_add, ))
                logging.info(msg="Был осуществлён запрос на добавление отчёта")
                return True
            except Exception as ex:
                logging.exception(msg="Сбой, запись в Report не была внесена")
                return False

    @staticmethod
    async def del_report_by_tg_id(tg_id: int) -> bool:
        """
        Асинхронный метод для удаления отчёта по tg_id
        """

        logging.info(msg="Был осуществлён запрос на удаление отчёта")
        with db.connect_to_db.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM Reports WHERE tg_id = (%s)", (tg_id, ))
                return True
            except Exception as ex:
                logging.exception(msg="Сбой, удаление записи из таблицы Report не была совершена")
                return False

    @staticmethod
    async def del_report_by_id(id: int) -> bool:
        """
        Асинхронный метод на удаление записи по id - Первичному ключу
        """

        with db.connect_to_db.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM Reports WHERE history_id = (%s)", (id, ))
                return True
            except Exception as ex:
                logging.critical(msg="Не удалось удалить отчёт")
                return False

    @staticmethod
    async def get_report_by_tg_id(tg_id: int) -> list | bool:
        """
        Асинхронный метод на получение записи по tg_id
        """

        logging.info(msg="Был осуществлён запрос на получение отчёта по tg_id")
        with db.connect_to_db.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM Reports WHERE tg_id = (%s)", (tg_id, ))

                response_data: list = cursor.fetchall()
                if cursor:
                    return response_data
                else:
                    return False

            except Exception as ex:
                logging.critical(msg="Не удалось получить отчёт по tg_id")
                return False

    @staticmethod
    async def get_report_by_id(id: int) -> list | bool:
        """
        Асинхронный метод на получение записи по id - Первичному ключу
        """

        logging.info(msg="Был осуществлён запрос на получение отчёта по tg_id")
        with db.connect_to_db.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM Reports WHERE history_id = (%s)", (id, ))

                response_data: list = cursor.fetchall()
                if cursor:
                    return response_data
                else:
                    return False

            except Exception as ex:
                logging.critical(msg="Не удалось получить отчёт по tg_id")
                return False

    @staticmethod
    async def get_all_reports() -> list | bool:
        """
        Асинхронный метод на получение всех записей из таблицы Reports
        """

        with db.connect_to_db.cursor() as cursor:
            cursor.execute("SELECT * FROM Reports")
            all_data: list = cursor.fetchall()

            if all_data: return True
            return False