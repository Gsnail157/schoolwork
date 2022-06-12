# Classes are a blueprint for creating new objects that have their own methods
# Object instance of a class

# Example

# Class : Human
# Object: John, Gary, Mary

class Robot:  # Use Capital in words and no spaces when creating a new class
    # "Self" refers to the object and is a attribute related to the object NOT THE CLASS ITSELF
    def introduce_self(self):
        print("My name is " + self.name)  # YOU MUST HAVE SELF AS A PARAMETER


r1 = Robot()  # Creating attributes the dirty way
r1.name = "Tom"
r1.color = "Red"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "Blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()

#   This is lengthly and not clean code
#   WE can use contructors to prevent typing attribute manually


class Person:
    # Contructors / Must have "self" as the first parameter + other parameters
    def __init__(self, name, color, weight):  # Special Method called a magic method
        self.name = name  # p1 name = name
        self.color = color  # p1 color = color
        self.weight = weight

    def introduction(self):
        print("My name is " + self.name)


p1 = Person("Gary", "Blue", 130)
p2 = Person("Molly", "Pink", 150)

p1.introduction()
p2.introduction()

# Defining Properties


# Inheritance: Used if you have different classes but share similar functions. Prevents repeating lines of code
# Inheritance is good but avoid multi-level inheritance as it makes the code unnessaryliy complex.
# Must use it correctly for Multi-level and Multiple inheritance to be a good thing

# class Mammal:
#   def eat(self):
#         print("Eat")

#   def walk(self):
#         print("Walk")

# class Fish:
#   def eat(self):
#         print("Eat")

#   def swim(self):
#         print("Swim")


class Animal:  # This Animal class is inherince from the object class with the default inheritance.
    # Therefore all Objects have access to the default methods
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")

# Animal: Parent or Base Class
# Mammal: Child or Sub Class


class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("Swim")


m = Mammal()
m.eat()
print(m.age)

# Another example of


class Dog:
    def __init__(self, name, age):  # Attributes
        self.name = name   # Where the data is stored
        self.age = age

    def bark(self):
        print("Bark")

    def get_name(self):  # Access the data
        return self.name

    def get_age(self):  # Access the data
        return self.age

    def set_age(self, age):  # Example of modifying data
        self.age = age


poodle = Dog("Doge", 23)
poodle.set_age(30)
print(poodle.get_age())

# More complex example and use of classes/ the benefits of using classes


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.get_grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("Success")
        else:
            print("Full Class")

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value = + student.self_grade()

        return value / len(self.students)


s1 = Student("Gary", 18, 80)
s2 = Student("Kelly", 16, 30)
s3 = Student("Molly", 49, 90)

# This course object that we created stores all of the students in the class and their attributes
c1 = Course("Math", 2)
c1.add_student(s1)
c1.add_student(s2)
print(c1.students[0].name)
c1.add_student(s3)
print(c1.students)

# Class Attributes & Methods


class Human:
    number_of_people = 0  # Class attributes dont have self and arent specific to any objects

    def __init__(self, name):
        self.name = name
        Human.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


Human.number_of_people = 10
h1 = Human("Gary")
h2 = Human("Molly")
print(Human.number_of_people_())  # Specific to the Class only


# Static Class Method


class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")


Math.add10(3)
