import logging

from fastapi import APIRouter
from src.api.schemas.historyevents import *
from src.api.services.historyevent import HistoryEventServiceAPI


history_event_router: APIRouter = APIRouter(prefix="/history_event", tags=["HistoryEvent"])


@history_event_router.get("/all")
async def get_all_hs_events() -> list[HistoryEvent] | dict:
    """
    Получение всех историй
    """

    try:
        response = await HistoryEventServiceAPI.get_all_events()
        return response
    except Exception as ex:
        logging.exception(msg="Не удалось получить все истории")
        return {"message": "Error"}


@history_event_router.get("/by_id")
async def get_event_by_id(id: int) -> HistoryEvent | dict:
    """
    Получение истории по id
    """

    try:
        response = await HistoryEventServiceAPI.get_event_by_id(id=id)
        return response
    except Exception as ex:
        logging.exception(msg="Не удалось получить историю по id")
        return {"message": "Error"}


@history_event_router.get("/by_tg_id")
async def get_event_by_id(tg_id: int) -> HistoryEvent | dict:
    """
    Получение истории по id
    """

    try:
        response = await HistoryEventServiceAPI.get_event_by_tg_id(tg_id=tg_id)
        return response
    except Exception as ex:
        logging.exception(msg="Не удалось получить историю по id")
        return {"message": "Error"}


@history_event_router.post("/add_event")
async def add_new_event(new_event: AddHistoryEvent) -> dict[str, str]:
    """
    Добавление новой истории
    """

    try:
        response = await HistoryEventServiceAPI.add_event(new_history=new_event)
        if response:
            return {"message": "Success"}
        raise ValueError("Ошибка при добавлении истории")
    except Exception as ex:
        logging.exception(msg="Не удалось добавить историю")
        return {"message": "Error"}


@history_event_router.delete("/by_id")
async def delete_event_by_id(id: int) -> dict[str, str]:
    """
    Удаление истории по id
    """

    try:
        response = await HistoryEventServiceAPI.del_history_by_id(id=id)
        if response:
            return {"message": "Success"}
        raise ValueError("Ошибка при удалении истории по id")
    except Exception as ex:
        logging.exception(msg="Не удалось получить историю по id")
        return {"message": "Error"}


@history_event_router.delete("/by_tg_id")
async def delete_event_by_id(tg_id: int) -> dict[str, str]:
    """
    Удаление истории по tg id
    """

    try:
        response = await HistoryEventServiceAPI.del_history_by_tg_id(tg_id=tg_id)
        if response:
            return {"message": "Success"}
        raise ValueError("Ошибка при удалении истории по id")
    except Exception as ex:
        logging.exception(msg="Не удалось получить историю по id")
        return {"message": "Error"}