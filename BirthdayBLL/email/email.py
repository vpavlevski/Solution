class Email:
    def __init__(self, fromPerson, toPerson, subject, message):
        self.fromPerson = fromPerson
        self.toPerson = toPerson
        self.subject = subject
        self.message = message

    @property
    def From(self): return self.fromPerson

    @property
    def To(self): return self.toPerson

    @property
    def Subject(self): return self.subject

    @property
    def Message(self): return self.message

    def ToString(self):
        return "From: " + self.fromPerson + " To: " + self.toPerson + " Subject: " + self.subject + " Message: " + self.message