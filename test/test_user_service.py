# Сторонние директории
import datetime
import unittest

# Локальные директории
from src import get_all_users, del_all_users, del_user, post_user, update_user_name
from src import UserInfo

class TestDataBase(unittest.IsolatedAsyncioTestCase):
    """
        Тестирование таблицы  - 'Users'
    """

    async def test_get_users(self):
        data = await get_all_users()

        # Проверка на пустоту таблицы
        self.assertEqual(type(data), bool)

        # Проверка на вывод функции
        self.assertEqual(len(data) > 1, True)

    async def test_del_user(self):
        #Проверка на возможность удаления пользователя
        data = await del_user(2389298392)
        self.assertEqual(data, True)

        # Проверка на пустую таблицу
        data_repeat = await del_user(2389298392)
        self.assertEqual(data_repeat, False)

        # Проверка на неправильный аргумент
        data_repeat = await del_user("Dsadasd")
        self.assertEqual(data_repeat, False)

        # Проверка на возможность удалить всех пользователей
        self.assertEqual(await del_all_users(), True)

    async def test_post_user(self):
        # Проверка на создание записи
        data = await post_user(UserInfo("Владимир", 35345345345, datetime.datetime.now()))
        self.assertEqual(data, True)

        # Проверка уже зарегистрированного пользователя
        self.assertEqual(data, "Вы уже зарегистрированы!")


    async def test_update_info_user(self):
        #Проверка на возможность изменения информации о пользователе
        self.assertEqual(await update_user_name("Николай", 35345345345), True)


if __name__ == "__main__":
    unittest.main()