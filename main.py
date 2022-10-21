from BirthdayBLL.email.email_sender import EmailSender
from BirthdayBLL.person.persons import Persons
from IO.CSVFileReader import CsvFileReader
from configuration import MAIL_TRAP_SERVER, BIRTHDAYS_FILE_PATH, CreateEmailFromTemplate, ADMIN_EMAIL, SEVEN_DAYS

emailSender = EmailSender(MAIL_TRAP_SERVER)

with CsvFileReader(BIRTHDAYS_FILE_PATH) as csvOpenFileReaderResult:
    csvOpenFileReaderResult\
    .OnError(lambda errorMessage : print(errorMessage))\
    .OnSuccess(lambda csvFile :
        Persons.CreatePersonArrayFromStringArray(csvFile.GetAllLinesAsStringArray())
            .HasAny(lambda persons:
                persons.ForEachPersonHavingBirthdayIn(SEVEN_DAYS, lambda birthdayPerson :
                    persons.GetAllPersonsExcept(birthdayPerson)
                        .ForEachPerson(lambda nonBirthdayPerson :
                            emailSender.SendEmail(CreateEmailFromTemplate(ADMIN_EMAIL, nonBirthdayPerson, birthdayPerson))
                            .OnSuccess(lambda infoMessage : print(infoMessage))
                            .OnError(lambda errorMessage : print(errorMessage))))))
print("Done")