# Exercise 04 of "Learn Python3 the Hard Way"
# Variables and Names

# how many cars
cars = 100
# seats in a car
space_in_a_car = 4.0
# how many drivers
drivers = 30
# how many passengers
passengers = 90
# how many cars without driver
cars_not_driven = cars - drivers
# how many cars have driver
cars_driven = drivers
# seats available of a car with driver
carpool_capacity = cars_driven * space_in_a_car
# average people amount in each car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
