from utils.guards.array_guards import array_has_exactly
from utils.validation.validation_rule import ValidationRule


class InputArrayValidationRule(ValidationRule):
    def execute(self, parameter):
        array_has_exactly(parameter, 3)