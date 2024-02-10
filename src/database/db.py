import psycopg2
import logging
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
                               "photo bytea,"
                               "user_id bigint REFERENCES Users (user_id));")

                cursor.execute("CREATE TABLE IF NOT EXISTS HistoryEvents("
                               "history_id serial PRIMARY KEY,"
                               "message_history varchar,"
                               "date_message timestamp,"
                               "user_id bigint REFERENCES Users (user_id),"
                               "event_id bigint REFERENCES Events (event_id));")

                self.connect_to_db.commit()

        except Exception as ex:
            logging.exception(msg="Не удалось подключиться к БД")

        finally:
            logging.info(msg="Подключение к БД завершилось.")
