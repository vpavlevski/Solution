from utils.guards.date_guards import is_valid_date_from_formats
from utils.templates.date_constants import DATE_FORMATS
from utils.validation.validation_rule import ValidationRule


class DateValidationRule(ValidationRule):
    def execute(self, parameter):
        is_valid_date_from_formats(parameter[2], DATE_FORMATS, "Birthday Date")