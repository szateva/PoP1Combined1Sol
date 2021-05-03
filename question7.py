class Person:
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName

    def get_info(self):
        return self._firstName + " " + self._lastName

    def get_name(self):
        return (self._firstName, self._lastName)




class Adult(Person):
    def __init__(self, firstName, lastName, phoneNum):
        super().__init__(firstName, lastName)
        self._phoneNum = phoneNum

    def get_phone(self):
        return self._phoneNum


class Child(Person):
    def __init__(self, firstName, lastName, parent1, parent2):
        super().__init__(firstName, lastName)
        self._parent1 = parent1
        self._parent2 = parent2


    def get_info(self):
        return super().get_info() + " " + self._parent1.get_info() + " " + self._parent2.get_info()

    def get_parents(self):
        return (self._parent1, self._parent2)


p = Person("Mary", "Ann")
a = Adult("John", "Doe", "1234567")
c = Child("Richard", "Doe", p, a)

assert a.get_info()== "John Doe" #must be True
assert c.get_name()==("Richard", "Doe") #must be True
assert c.get_info()== "Richard Doe Mary Ann John Doe" #must be True
assert c.get_parents() == (p,a) #must be True