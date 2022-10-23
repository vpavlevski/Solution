from utils.guards.string_guards import string_is_none_or_empty, string_is_valid_email_address
from utils.validation.validation_rule import ValidationRule


class EmailValidationRule(ValidationRule):
    def Execute(self, parameter):
        string_is_none_or_empty(parameter[1], "Email")
        string_is_valid_email_address(parameter[1], "Email")