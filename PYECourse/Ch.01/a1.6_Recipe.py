# Ch.01 Exercise 1.5
# Recipe combination

diet = ["Tomato", "Brocoli", "Steak", "Cucumber", "Shrimp"]
for x in range(0, 5):
    for y in range(x, 5):
        if not (x == y):
            print("{} {}".format(diet[x], diet[y]))
