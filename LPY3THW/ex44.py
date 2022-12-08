# Exercise 44 of "Learn Python3 the Hard Way"
# Inheritance versus Composition

# Parent-Child is-a relationship


class Parent(object):
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

print("Parent-Child is-a relationship.")
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

##########

# Child has-a Other; "has-a" relationship


class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class ChildO(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


print('\nChildO has-a Other; "has-a" relationship')

sonO = ChildO()

sonO.implicit()
sonO.override()
sonO.altered()
