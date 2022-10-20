from Utils.Guards.date_guards import is_valid_date_from_formats
from Utils.Templates.date_constants import DATE_FORMATS
from Utils.Validation.validation_rule import ValidationRule


class DateValidationRule(ValidationRule):
    def Execute(self, parameter):
        is_valid_date_from_formats(parameter[2], DATE_FORMATS, "Birthday Date")