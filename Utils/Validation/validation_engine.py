class ValidationEngine():

    def __init__(self):
        self.rules = []

    def AddRule(self, validationRule):
        self.rules.append(validationRule)
        return self

    def Execute(self, parameter):
        for rule in self.rules:
            rule.Execute(parameter)