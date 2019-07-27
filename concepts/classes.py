# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class


class User:
    # Constructor
    # self is like this keyword
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method with f dtring

    def greetings(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# init User object
Javed = User('javed Khalil', 26)
Janet = User('Janet', 22)
# call objects
print(Javed.name)
print(Javed.age)

# Edit property
Javed.age = 28
print('Age cahnged >> ', Javed.age)

# call method // function // methods or functions have () paranthesis
print(Javed.greetings())

# birthday
print('Janet Age >> ', Janet.age)
Janet.has_birthday()
print('Janet New Age >> ', Janet.age)

################
# INHERITANCE
################


class Customer(User):
    # Constructor
    # self is like this keyword
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def greetings(self):
        return f'{self.name} is a customer'


# init Customer object
John = Customer('John', 23, 12345)

print(John.name)
print(John.age)
print(John.ID)

# method overide
print(John.greetings())
print(Javed.greetings())
