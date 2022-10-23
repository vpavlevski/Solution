from birthday_bll.email.email_sender import EmailSender
from birthday_bll.person.persons import Persons
from input_output.csv_file_reader import CsvFileReader
from configuration import MAIL_TRAP_SERVER, BIRTHDAYS_FILE_PATH, CreateEmailFromTemplate, ADMIN_EMAIL, SEVEN_DAYS

emailSender = EmailSender(MAIL_TRAP_SERVER)

with CsvFileReader(BIRTHDAYS_FILE_PATH) as csvOpenFileReaderResult:
    csvOpenFileReaderResult\
    .on_error(lambda errorMessage : print(errorMessage))\
    .on_success(lambda csvFile :
        Persons.create_person_array_from_string_array(csvFile.get_all_lines_as_string_array())
                .has_any(lambda persons:
                persons.for_each_person_having_birthday_in(SEVEN_DAYS, lambda birthdayPerson :
                    persons.get_all_persons_except(birthdayPerson)
                                                           .for_each_person(lambda nonBirthdayPerson :
                            emailSender.send_email(CreateEmailFromTemplate(ADMIN_EMAIL, nonBirthdayPerson, birthdayPerson))
                                                                            .on_success(lambda infoMessage : print(infoMessage))
                                                                            .on_error(lambda errorMessage : print(errorMessage))))))
print("Done")