import string
from datetime import datetime, timedelta

from Utils.Guards.date_guards import CreateDateTimeFromString
from Utils.Templates.date_constants import MONTH_DAY_FORMAT
from Utils.TypeUtils.DateTimeUtils import ConvertToMonthDayDateTime


class DateTimeAdapter:
    def __init__(self, dateTime: datetime):
        self.dateTime = dateTime

    @property
    def DateTime(self): return self.dateTime

    @classmethod
    def CreateFromString(cls, value: string):
        return DateTimeAdapter(CreateDateTimeFromString(value))

    @classmethod
    def Now(cls):
        return DateTimeAdapter(datetime.now())

    def ConvertToMonthDayDateTime(self):
        return DateTimeAdapter(ConvertToMonthDayDateTime(self.dateTime.strftime(MONTH_DAY_FORMAT)))

    def SubtractDays(self, days):
        return DateTimeAdapter(self.dateTime - timedelta(days))

    def SubtractDate(self, date) -> timedelta:
        return self.dateTime - date.dateTime

    def ToString(self, format):
        return self.dateTime.strftime(format)