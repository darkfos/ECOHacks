import logging

from fastapi import FastAPI
from src.api.schemas.historyevents import *
from src.database.services.historyevent_service import HistoryEventServiceDB

from typing import Optional


class HistoryEventServiceAPI:

    @staticmethod
    async def get_event_by_id(id: int) -> bool | list[HistoryEvent]:
        """
        Получаем событие по id
        """

        try:
            events: Optional[bool, list] = await HistoryEventServiceDB.get_history_by_idp(id=id)

            if isinstance(events, bool): raise ValueError("Не были найдены события")
            return [HistoryEvent(
                history_event_id = events[0],
                message_history = events[1],
                date_message = events[2],
                tg_id = events[-1]
            )
                for event in events
            ]
        except Exception as ex:
            logging.exception(msg="Не удалось получить событие по id")
            return False

    @staticmethod
    async def get_event_by_tg_id(tg_id: int) -> bool | list[HistoryEvent]:
        """
        Получаем событие по id
        """

        try:
            events: Optional[bool, list] = await HistoryEventServiceDB.get_history_by_id(tg_id=tg_id)

            if isinstance(events, bool): raise ValueError("Не были найдены события")
            return [HistoryEvent(
                history_event_id = events[0],
                message_history = events[1],
                date_message = events[2],
                tg_id = events[-1]
            )
                for event in events
            ]
        except Exception as ex:
            logging.exception(msg="Не удалось получить событие по id")
            return False

    @staticmethod
    async def get_all_events() -> bool | list[HistoryEvent]:
        """
        Получение все event
        """

        try:
            response_db = await HistoryEventServiceDB.get_all_histories()

            all_events = [HistoryEvent(
                history_event_id = event[0],
                message_history = event[1],
                date_message = event[2],
                tg_id = event[-1]
            )
                          for event in response_db]

            return all_events
        except Exception as ex:
            logging.exception(msg="Не удалось получить события")
            return False

    @staticmethod
    async def add_event(new_history: AddHistoryEvent) -> bool:
        """
        Добавление истории
        """

        try:
            events: bool = await HistoryEventServiceDB.post_history(history_data=new_history)
            return events
        except Exception as ex:
            logging.exception(msg="Не удалось получить событие по id")
            return False

    @staticmethod
    async def del_history_by_tg_id(tg_id: int) -> bool:
        """
        Удаление истории по tg id
        """

        try:
            events: bool = await HistoryEventServiceDB.del_history(tg_id=tg_id)
            return events
        except Exception as ex:
            logging.exception(msg="Не удалось получить событие по id")
            return False

    @staticmethod
    async def del_history_by_id(id: int) -> bool:
        """
        Удаление истории по id
        """

        try:
            events: bool = await HistoryEventServiceDB.del_history_by_idp(id=id)
            return events
        except Exception as ex:
            logging.exception(msg="Не удалось получить событие по id")
            return False