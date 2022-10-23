from birthday_bll.person.person import Person
from utils.collections.string_array import StringArray


class Persons:
    def __init__(self):
        self.personArray = []

    @classmethod
    def create_person_array_from_string_array(cls, stringArray: StringArray):
        resultArray = Persons()
        stringArray.for_each_line(lambda line: Person.create_from_string(line).on_success(resultArray.add_person).on_error(lambda errMessage : print(errMessage)))
        return resultArray

    def add_person(self, person):
        self.personArray.append(person)

    def has_any(self, callback):
        if self.count()<=0:
            return
        callback(self)

    def for_each_person_having_birthday_in(self, numberOfDays, callback):
        for p in self.personArray:
            if p.has_birthday_in(numberOfDays):
                callback(p)

    def get_all_persons_except(self, person):
        newPersons = Persons()
        for p in self.personArray:
            if p.UUID != person.UUID:
                newPersons.add_person(p)
        return newPersons

    def for_each_person(self, callback):
        for p in self.personArray:
            callback(p)

    def count(self):
        return len(self.personArray)