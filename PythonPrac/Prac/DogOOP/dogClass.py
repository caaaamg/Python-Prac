#OOP Dog as example

import datetime #Datetime library


class Dog: #Class to contain all Dog methods/attributes

    walkies = 0 #Class variable for tracking walks

    def __init__(self, name, breed, age, gender): #Template Dog
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

    def print_details(self): #function to print all data
        details = "Name = {} \nBreed = {} \nAge = {} \nGender = {}".format(self.name, self.breed, self.age, self.gender)
        return print(details)

    def gone_for_walk(self): #Walk update
        self.walkies += 1
        return "{} has gone for a walk! Total walkies = {}".format(self.name, self.walkies)

    def dog_birthday(self): #Age update for birthday
        self.age += 1
        return "Happy Birthday {}! {} is {} years old today!".format(self.name, self.name, self.age)

    @staticmethod #static method to check if day is on walking schedule - Tues/Thurday/Saturday
    def is_walk_day(day):
        if day.weekday() % 2 == 0:
            return 'Time to walk the dogs!'
        return 'Rest day'



dog1 = Dog('Trudy', 'Boxer', 7, 'Female')
dog2 = Dog('Neville', 'French Bulldog', 4, 'Male')
dog3 = Dog('Rupert', 'Pinscher', 9, 'Male')
dog4 = Dog('Hugo', 'Golden Retriever', 12, 'Male')
dog5 = Dog('Luna', 'Labradoodle', 2, 'Female')


print(dog2.print_details())
print(dog5.gone_for_walk())

print(dog3.dog_birthday())


my_date = datetime.date(2020, 8, 10)
print(Dog.is_walk_day(my_date))
