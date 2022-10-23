import uuid

from birthday_bll.person_validation.date_validation_rule import DateValidationRule
from birthday_bll.person_validation.email_validation_rule import EmailValidationRule
from birthday_bll.person_validation.input_array_validation_rule import InputArrayValidationRule
from birthday_bll.person_validation.name_validation_rule import NameValidationRule
from utils.operation import OperationResult
from utils.templates.date_constants import YEAR_MONTH_DAY_FORMAT
from utils.type_adapters.date_time_adapter import DateTimeAdapter
from utils.validation.validation_engine import ValidationEngine


class Person:

    def __init__(self, name, email, birthday):
        self.uuid = uuid.uuid1()
        self.name = name
        self.email = email
        self.birthdayDate = DateTimeAdapter.CreateFromString(birthday)

    @property
    def UUID(self):
        return self.uuid

    @property
    def Name(self): return self.name

    @property
    def Birthday(self)->DateTimeAdapter: return self.birthdayDate

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
        return DateTimeAdapter.Now().ConvertToMonthDayDateTime()\
                   .SubtractDate(self.birthdayDate.ConvertToMonthDayDateTime().SubtractDays(numberOfDays))\
                   .days==0

    def ToString(self):
        return "Name: " + str(self.name) + " Email: " + str(self.email) + " Birthday: " + self.birthdayDate.ToString(YEAR_MONTH_DAY_FORMAT)

