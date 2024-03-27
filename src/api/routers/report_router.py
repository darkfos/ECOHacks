import logging

from fastapi import APIRouter
from src.api.schemas.reports import Report, AddReport
from src.api.services.report import ReportServiceAPI
from typing import Optional


report_router: APIRouter = APIRouter(prefix="/reports", tags=["Report"])


@report_router.get("/all")
async def get_all_reports() -> list[Report] | dict:
    """
    Получение всех отчетов
    """

    data_report: Optional[list, bool] = await ReportServiceAPI.get_all_reports()

    try:
        if type(data_report) is bool:
            raise ValueError("Не удалось получить отчёты")
        else:
            return data_report
    except Exception as ex:
        logging.exception(msg="Не удалось получить все отчеты")
        return {
            "message": "Error"
        }


@report_router.get("/report_id")
async def get_report_by_id(id: int) -> Report | dict:
    """
    Получение отчета по id
    """

    try:
        data_report: Optional[Report, bool] = await ReportServiceAPI.get_report_by_id(id=id)

        if type(data_report) is bool:
            raise ValueError("Ошибка получения отчета по id")
        else:
            return data_report
    except Exception as ex:
        logging.exception(msg="Не удалось получить отчет по id")
        return {
            "message": "Error"
        }


@report_router.get("/report_tg_id")
async def get_report_by_tg_id(tg_id: int) -> list[Report] | dict:
    """
    Получение всех отчетов по tg_id
    """

    try:
        all_reports_by_tg_id: list[Report] = await ReportServiceAPI.get_report_by_tg_id(tg_id=tg_id)

        if type(all_reports_by_tg_id) is bool:
            raise ValueError("Ошибка получения отчетов по tg_id")
        else:
            return all_reports_by_tg_id
    except Exception as ex:
        logging.exception(msg="Не удалось получить отчеты по tg_id")
        return {
            "message": "Error"
        }


@report_router.post("/add_report")
async def add_new_report(new_report: AddReport) -> dict:
    """
    Добавление нового отчета
    """

    try:
        add_report = await ReportServiceAPI.add_report(new_report=new_report)
        if add_report:
            return {"message": "Success"}
        else:
            raise ValueError("Ошибка при добавлении отчёта")
    except Exception as ex:
        logging.exception(msg="Не удалось добавить отчет")
        return {"message": "Error"}


@report_router.delete("/report_id")
async def delete_report_by_id(id: int) -> dict:
    """
    Удаление отчета по id
    """

    try:
        to_del: bool = await ReportServiceAPI.del_report_by_id(id=id)
        if to_del:
            return {"message": "Success"}
        else:
            raise ValueError("Ошибка удаления отчёта по id")
    except Exception as ex:
        logging.exception(msg="Не удалось удалить отчет по id")
        return {"message": "Error"}


@report_router.delete("/report_tg_id")
async def delete_report_by_id(tg_id: int) -> dict:
    """
    Удаление отчета по id
    """

    try:
        to_del: bool = await ReportServiceAPI.del_report_by_tg_id(tg_id=tg_id)
        if to_del:
            return {"message": "Success"}
        else:
            raise ValueError("Ошибка удаления отчёта по tg id")
    except Exception as ex:
        logging.exception(msg="Не удалось удалить отчет по tg id")
        return {"message": "Error"}