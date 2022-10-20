import uuid
from datetime import timedelta, datetime

from BirthdayBLL.person_validation.date_validation_rule import DateValidationRule
from BirthdayBLL.person_validation.email_validation_rule import EmailValidationRule
from BirthdayBLL.person_validation.input_array_validation_rule import InputArrayValidationRule
from BirthdayBLL.person_validation.name_validation_rule import NameValidationRule
from Utils.Operation import OperationResult
from Utils.Templates.date_constants import MONTH_DAY_FORMAT
from Utils.TypeUtils.DateTimeUtils import ConvertToMonthDayDateTime
from Utils.Validation.validation_engine import ValidationEngine


class Person:

    def __init__(self, name, email, birthday):
        self.uuid = uuid.uuid1()
        self.name = name
        self.email = email
        self.birthday = birthday

    @property
    def UUID(self):
        return self.uuid

    @property
    def Name(self): return self.name

    @property
    def Birthday(self): return self.birthday

    @property
    def Email(self): return self.email

    @classmethod
    def CreateFromString(self, line):
        try:
            ValidationEngine()\
                .AddRule(InputArrayValidationRule())\
                .AddRule(NameValidationRule())\
                .AddRule(EmailValidationRule())\
                .AddRule(DateValidationRule())\
            .Execute(line)

            return OperationResult.CreateSuccess(Person(line[0].strip(),line[1].strip(),line[2].strip()))
        except Exception as e:
            return OperationResult.CreateError("Error: " + str(e))

    def HasBirthdayIn(self, numberOfDays):
        birthday = ConvertToMonthDayDateTime(self.birthday)

        sendReminderAt = birthday - timedelta(numberOfDays)
        currentDate = datetime.strptime(datetime.now().strftime(MONTH_DAY_FORMAT), MONTH_DAY_FORMAT)

        delta = currentDate - sendReminderAt
        return delta.days == 0

    def ToString(self):
        return "Name: " + str(self.name) + " Email: " + str(self.email) + " Birthday: " + str(self.birthday)

