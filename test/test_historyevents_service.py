import datetime
import unittest

# Локальные директории
from src import get_all_histories, get_history_by_id, post_history, del_history
from src import HistoryEventInfo

class TestHistoryEventDataBase(unittest.IsolatedAsyncioTestCase):
    """
    Тестирование таблицы - 'HistoryEvents'
    """

    async def test_post_history(self):
        # Проверка на создание истории о событии
        data_to_add: HistoryEventInfo = HistoryEventInfo("Убрал мусор у площадки", datetime.datetime.now(), 35345345345)
        self.assertEqual(await post_history(data_to_add), True)

    async def test_get_history(self):
        # Проверка на получение массива всех историй
        self.assertEqual(type(await get_all_histories()), list)

        # Проверка на получение пустого массива всех историй
        self.assertEqual(await get_all_histories(), False)

    async  def test_del_history(self):
        # Проверка на удаление записи истории
        self.assertEqual(await del_history(35345345345), True)

        # Проверка на не существующий tg_id
        self.assertEqual(await del_history(23123123123), False)


if __name__ == "__main__":
    unittest.main()