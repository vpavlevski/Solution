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
        self.birthdayDate = DateTimeAdapter.create_from_string(birthday)

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
    def create_from_string(self, line):
        try:
            ValidationEngine()\
                .add_rule(InputArrayValidationRule())\
                .add_rule(NameValidationRule())\
                .add_rule(EmailValidationRule())\
                .add_rule(DateValidationRule())\
            .execute(line)

            return OperationResult.create_success(Person(line[0].strip(), line[1].strip(), line[2].strip()))
        except Exception as e:
            return OperationResult.create_error("Error: " + str(e))

    def has_birthday_in(self, numberOfDays):
        return DateTimeAdapter.now().convert_to_month_day_date_time()\
                   .subtract_date(self.birthdayDate.convert_to_month_day_date_time().subtract_days(numberOfDays))\
                   .days==0

    def to_string(self):
        return "Name: " + str(self.name) + " Email: " + str(self.email) + " Birthday: " + self.birthdayDate.to_string(YEAR_MONTH_DAY_FORMAT)

