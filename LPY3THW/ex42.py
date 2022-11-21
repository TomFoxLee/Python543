# Exercise 42 of "Learn Python3 the Hard Way"
# Is-A, Has-A, Objects, and Classes
#
# add "# type: ignore" at line end if need to bypass type error

# Animal is-a object (yes, sort of coufusing) look at the exrea credit
class Animal(object):
    pass


## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name


## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name


## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


## ??
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary


## ??
class Fish(object):
    pass


## ??
class Salmon(Fish):
    pass


## ??
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan  # type: ignore

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover  # type: ignore

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
