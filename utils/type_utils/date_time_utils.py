from datetime import datetime
from utils.templates.date_constants import MONTH_DAY_FORMAT, YEAR_MONTH_DAY_FORMAT


def convert_to_month_date_time(inputDateTime):
    try:
        return datetime.strptime(inputDateTime, MONTH_DAY_FORMAT)
    except:
        dt = datetime.strptime(inputDateTime, YEAR_MONTH_DAY_FORMAT)
        return datetime.strptime(str(dt.month)+"-"+str(dt.day),MONTH_DAY_FORMAT)