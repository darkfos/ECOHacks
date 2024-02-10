# Сторонние директори
import datetime
import unittest

# Локальные директории
from src import get_all_events, get_event_by_id, del_events, post_event
from src import EventInfo

class TestEventDataBase(unittest.IsolatedAsyncioTestCase):
    """
        Тестирование таблицы  - 'Events'
    """

    async def test_post_events(self):
        # Проверка на создание События по не сущестующему tg_id в таблице Users
        data_to_add: EventInfo = EventInfo(23213443, "Мусор у подножья горы!", datetime.datetime.now(), b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b')
        self.assertEqual(await post_event(data_to_add), False)

        # Проверка на создание События по существующему tg_id в таблице Users
        data_to_add: EventInfo = EventInfo(35345345345, "Мусор у подножья горы!", datetime.datetime.now(), b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b')
        self.assertEqual(await post_event(data_to_add), True)

    async def test_get_events(self):
        # Проверка на получение пустого массива данных
        self.assertEqual(await get_all_events(), False)

        # Проверка на получение не пустого массива данных
        self.assertEqual(type(await get_all_events()), list)

        # Проверка на получение События по tg_id
        self.assertEqual(type(await get_event_by_id(35345345345)), list)

        # Проверка на не на получение События по tg_id
        self.assertEqual(await get_event_by_id(24324234), False)

    async def test_delete_events(self):
        # Проверка на удаление события
        self.assertEqual(await del_events(35345345345), True)

if __name__ == "__main__":
    unittest.main()

