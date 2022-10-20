import re

def string_is_valid_email_address(parameter, parameterName):
    if (re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', parameter.strip())):
        return
    raise Exception("Parameter '" + parameterName + "' is not a valid email address: '" + parameter+"'")

def string_is_alpha(parameter, parameterName):
    if parameter.replace(" ","").isalpha():
        return
    raise Exception("Parameter '" + parameterName + "' has to contain only letters")

def string_is_none_or_empty(parameter, parameterName):
    if parameter and parameter.strip():
        return
    raise Exception("Parameter '" + parameterName + "' is empty!")
