class Human():
    def __init__(self, gender= "unknown", age = 0, name = "unknown"):
        self._gender = gender
        self._age = age
        self._name = name

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setGender(self, gender):
        if gender.lower() == 'male':
            self._gender = gender
        elif gender.lower() == 'female':
            self._gender = gender
        else:
            self._gender = "other"

    def getGender(self):
        return self._gender

# fred
fred = Human('Male')
fred.setname(
print(fred.getGender())
# & wilma
wilma = Human('female')
print(wilma.getGender())

# add another attribute called _name
# create some code to add a name to an instance of the class

# add another method to the Human class called
# speak() - which returns _name + ": says 'Hello'"
# note the single quotes
