# Сторонние директории
import psycopg2
import logging

# Локальные директории
from src import configuration

class Database:

    def __init__(self):

        try:
            self.connect_to_db = psycopg2.connect(configuration.URL_DB)
            self.connect_to_db.autocommit = True

            with self.connect_to_db.cursor() as cursor:
                #Создание таблиц
                cursor.execute("CREATE TABLE IF NOT EXISTS Users("
                               "user_id serial PRIMARY KEY,"
                               "name_user varchar(350),"
                               "tg_id bigint,"
                               "date_reg timestamp);")

                cursor.execute("CREATE TABLE IF NOT EXISTS Events("
                               "event_id serial PRIMARY KEY,"
                               "tg_id bigint,"
                               "message_event varchar,"
                               "date_event timestamp,"
                               "photo varchar,"
                               "user_id bigint REFERENCES Users (user_id) ON DELETE CASCADE ON UPDATE CASCADE);")

                cursor.execute("CREATE TABLE IF NOT EXISTS HistoryEvents("
                               "history_id serial PRIMARY KEY,"
                               "message_history varchar,"
                               "date_message timestamp,"
                               "user_id bigint REFERENCES Users (user_id) ON DELETE CASCADE ON UPDATE CASCADE,"
                               "event_id bigint REFERENCES Events (event_id) ON DELETE CASCADE ON UPDATE CASCADE);")

                cursor.execute("CREATE TABLE IF NOT EXISTS Reports("
                               "history_id serial PRIMARY KEY,"
                               "message_history varchar,"
                               "tg_id bigint,"
                               "street_data varchar,"
                               "latitude decimal,"
                               "longitude decimal,"
                               "photo varchar,"
                               "date_report timestamp)")

                self.connect_to_db.commit()

        except Exception as ex:
            logging.exception(msg="Не удалось подключиться к БД")

        finally:
            logging.info(msg="Подключение к БД завершилось.")
