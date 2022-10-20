from datetime import datetime


def is_valid_date_format(parameter, format, parameterName):
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