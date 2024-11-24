from datetime import datetime

class DateFormat:
    basis = "%Y-%m-%d"

    @staticmethod
    def format(date:datetime) -> str:
        return date.strftime(DateFormat.basis)

    @staticmethod
    def parse(date:str) -> datetime:
        return datetime.strptime(date, DateFormat.basis)