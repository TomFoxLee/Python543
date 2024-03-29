# Exercise 42 of "Learn Python3 the Hard Way"
# Is-A, Has-A, Objects, and Classes
#
# add "# type: ignore" at line end if need to bypass type error

# Animal is-a object (yes, sort of coufusing) look at the exrea credit
class Animal(object):
    pass


## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name


## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name


## Person is-a object
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass


## Salmon is-a Fish
class Salmon(Fish):
    pass


## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan  # type: ignore

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet
frank.pet = rover  # type: ignore

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
