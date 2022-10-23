from utils.guards.string_guards import string_is_none_or_empty, string_is_alpha
from utils.validation.validation_rule import ValidationRule


class NameValidationRule(ValidationRule):
    def execute(self, parameter):
        string_is_none_or_empty(parameter[0], "Person Name")
        string_is_alpha(parameter[0], "Person Name")