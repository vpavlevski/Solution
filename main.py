from BirthdayBLL.email.email_sender import EmailSender
from BirthdayBLL.person.PersonClass import Person
from BirthdayBLL.person.persons import Persons
from IO.CSVFileReader import CsvFileReader
from configuration import MAIL_TRAP_SERVER, BIRTHDAYS_FILE_PATH, CreateEmailFromTemplate, ADMIN_EMAIL, SEVEN_DAYS

emailSender = EmailSender(MAIL_TRAP_SERVER)

personArray = Persons()
with CsvFileReader(BIRTHDAYS_FILE_PATH) as csvOpenFileReaderResult:
    csvOpenFileReaderResult\
    .OnError(lambda errorMessage : print(errorMessage))\
    .OnSuccess(lambda csvFile : csvFile.ForEachLine(lambda line :
                                                        Person.CreateFromString(line)
                                                        .OnError(lambda errorMessage: print(errorMessage))
                                                        .OnSuccess(personArray.AddPerson)))
personArray.HasAny(lambda :
                   personArray.ForEachPersonHavingBirthdayIn(SEVEN_DAYS,lambda birthdayPerson :
                       personArray.GetAllPersonsExcept(birthdayPerson)
                       .ForEachPerson(lambda person :
                            emailSender.SendEmail(CreateEmailFromTemplate(ADMIN_EMAIL, person, birthdayPerson))
                                      .OnSuccess(lambda infoMessage : print(infoMessage))
                                      .OnError(lambda errorMessage: print(errorMessage)))))