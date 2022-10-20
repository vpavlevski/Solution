class Persons:
    def __init__(self):
        self.personArray = []

    def AddPerson(self, person):
        self.personArray.append(person)

    def HasAny(self, callback):
        if self.Count()<=0:
            return
        callback()

    def ForEachPersonHavingBirthdayIn(self, numberOfDays, callback):
        for p in self.personArray:
            if p.HasBirthdayIn(numberOfDays):
                callback(p)

    def GetAllPersonsExcept(self, person):
        newPersons = Persons()
        for p in self.personArray:
            if p.UUID != person.UUID:
                newPersons.AddPerson(p)
        return newPersons

    def ForEachPerson(self, callback):
        for p in self.personArray:
            callback(p)

    def Count(self):
        return len(self.personArray)