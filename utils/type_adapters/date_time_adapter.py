import string
from datetime import datetime, timedelta

from utils.guards.date_guards import CreateDateTimeFromString
from utils.templates.date_constants import MONTH_DAY_FORMAT
from utils.type_utils.date_time_utils import convert_to_month_date_time


class DateTimeAdapter:
    def __init__(self, dateTime: datetime):
        self.dateTime = dateTime

    @classmethod
    def create_from_string(cls, value: string):
        return DateTimeAdapter(CreateDateTimeFromString(value))

    @classmethod
    def now(cls):
        return DateTimeAdapter(datetime.now())

    def convert_to_month_day_date_time(self):
        return DateTimeAdapter(convert_to_month_date_time(self.dateTime.strftime(MONTH_DAY_FORMAT)))

    def subtract_days(self, days):
        return DateTimeAdapter(self.dateTime - timedelta(days))

    def subtract_date(self, date) -> timedelta:
        return self.dateTime - date.dateTime

    def to_string(self, format):
        return self.dateTime.strftime(format)
