import string

from birthday_bll.email.email import Email
from birthday_bll.person.person import Person
from utils.templates.date_constants import MONTH_DAY_FORMAT
from utils.type_adapters.date_time_adapter import DateTimeAdapter
from birthday_bll.email.email_server_settings import EmailServerSettings

MAIL_TRAP_SERVER = EmailServerSettings("smtp.mailtrap.io", 2525, "bc0ec192e22a2a", "3b4105b5961092", 3)
BIRTHDAYS_FILE_PATH = "./Birthdays.csv"
ADMIN_EMAIL="admin@Birthday.com"
SEVEN_DAYS=7

def CreateEmailFromTemplate(fromEmail: string, emailPerson: Person, birthdayPerson: Person):
    return Email(fromEmail, emailPerson.Email,
               "Birthday Reminder: {0}'s birthday on {1}".format(birthdayPerson.Name, birthdayPerson.Birthday.to_string(MONTH_DAY_FORMAT)),
               "Hi {0},\nThis is a reminder that {1} will be celebrating their birthday on {2}.\nThere are {3} days left to get a present!"
                 .format(emailPerson.Name, birthdayPerson.Name, birthdayPerson.Birthday.to_string(MONTH_DAY_FORMAT),
                         birthdayPerson.Birthday.convert_to_month_day_date_time().subtract_date(DateTimeAdapter.now().convert_to_month_day_date_time()).days))