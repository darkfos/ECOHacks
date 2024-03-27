import logging

from typing import Optional

from src.api.schemas.reports import AddReport, Report
from src.database.services.report_service import ReportServiceDB
from src.data_cls import ReportInfo


class ReportServiceAPI:

    @staticmethod
    async def get_report_by_tg_id(tg_id: int) -> list[Report] | bool:
        """
        Получение отчётов по tg id
        """

        try:
            all_data: Optional[list, bool] = await ReportServiceDB.get_report_by_tg_id(tg_id=tg_id)
            if isinstance(all_data, bool):
                raise ValueError("Ошибка получения отчётов на DB service")

            all_data_reports: list[Report] = [Report(
                report_id = report[0],
                message_history = report[1],
                tg_id = report[2],
                photo = report[3],
                latitude = report[4],
                longtitude = report[5],
                street_data = report[6],
                date_report = report[-1]
            ) for report in all_data]

            print(all_data_reports)
            return all_data_reports
        except Exception as ex:
            logging.exception(msg="Не удалось получить отчет по TG id")
            return False

    @staticmethod
    async def get_report_by_id(id: int) -> Report | bool:
        """
        Получение отчётов по id
        """

        try:
            report: Optional[list, bool] = await ReportServiceDB.get_report_by_id(id=id)

            if isinstance(report, bool):
                raise ValueError("Ошибка получения отчета по id в DB service")
            else:
                unique_report: Report = Report(
                    report_id = report[0],
                    message_history = report[1],
                    tg_id = report[2],
                    photo = report[3],
                    latitude = report[4],
                    longtitude = report[5],
                    street_data = report[6],
                    date_report = report[-1])

                return unique_report
        except Exception as ex:
            logging.exception(msg="Не удалось получить отчет по id")
            return False

    @staticmethod
    async def get_all_reports() -> list[Report] | bool:
        """
        Получение всех отчетов
        """

        try:
            all_reports: Optional[list, bool] = await ReportServiceDB.get_all_reports()
            print(all_reports)
            if isinstance(all_reports, bool):
                return False
            else:
                all_reports: list[Report] = [Report(
                    report_id = report[0],
                    message_history = report[1],
                    tg_id = report[2],
                    photo = report[3],
                    latitude = report[4],
                    longtitude = report[5],
                    street_data = report[6],
                    date_report = report[-1]
                )
                    for report in all_reports
                ]

                return all_reports
        except Exception as ex:
            logging.exception(msg="Не удалось получить все отчеты")


    @staticmethod
    async def add_report(new_report: AddReport) -> bool:
        """
        Добавление отчета, жалобы от User
        """

        try:
            await ReportServiceDB.post_report(data_report=ReportInfo(**new_report.dict()))
            return True
        except Exception as ex:
            logging.exception(msg="Не удалось добавить отчёт")
            return False

    @staticmethod
    async def del_report_by_tg_id(tg_id: int) -> bool:
        """
        Удаление отчета по tg_id
        """

        try:
            del_report: bool = await ReportServiceDB.del_report_by_tg_id(tg_id=tg_id)

            if del_report:
                return del_report
            raise ValueError("Ошибка при удалении отчета в DB service")
        except Exception as ex:
            logging.exception(msg="Не удалось удалить отчет по tg_id")
            return False

    @staticmethod
    async def del_report_by_id(id: int) -> bool:
        """
        Удаление отчета по id
        """

        try:
            del_report: bool = await ReportServiceDB.del_report_by_id(id=id)
            if del_report:
                return True
            raise ValueError("Ошибка при удалении отчета в DB service")
        except Exception as ex:
            logging.exception(msg="Не удалось удалить отчет по id")
            return False