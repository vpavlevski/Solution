class ValidationEngine():

    def __init__(self):
        self.rules = []

    def add_rule(self, validationRule):
        self.rules.append(validationRule)
        return self

    def execute(self, parameter):
        for rule in self.rules:
            rule.execute(parameter)