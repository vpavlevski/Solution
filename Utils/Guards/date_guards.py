import string
from datetime import datetime

from Utils.Templates.date_constants import DATE_FORMATS


def CreateDateTimeFromString(value: string)->datetime:
    for dateFormat in DATE_FORMATS:
        try:
            return datetime.strptime(value,dateFormat)
        except:
            pass
    raise ValueError("Incorrect DateTime Format")

def is_valid_date_format(parameter, format, parameterName)->bool:
    try:
        try_parse_date_format(parameter, format, parameterName)
        return True
    except:
        return False

def try_parse_date_format(parameter, format, parameterName):
    try:
        datetime.strptime(parameter.strip(), format)
        return
    except ValueError:
        raise ValueError("Incorrect data format for parameter '" + parameterName+ "', should be YYYY-MM-DD")

def is_valid_date_from_formats(parameter, formats, parameterName):
    for format in formats:
        try:
            datetime.strptime(parameter.strip(),format)
            return
        except:
            pass

    raise ValueError("Incorrect data format for parameter '" + parameterName+"', should be one of the following formats: YYYY-MM-DD or MM-DD")