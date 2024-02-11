# Локальные директивы
from ..db import Database
from src.data_cls import ReportInfo

# Внешние директивы
import logging


db = Database()


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


async def del_report(tg_id: int) -> bool:
    """
    Асинхронный метод для удаления отчёта
    """

    logging.info(msg="Был осуществлён запрос на удаление отчёта")
    with db.connect_to_db.cursor() as cursor:
        try:
            cursor.execute("DELETE FROM Reports WHERE tg_id = (%s)", (tg_id, ))
            return True
        except Exception as ex:
            logging.exception(msg="Сбой, удаление записи из таблицы Report не была совершена")
            return False