# Ch.03 Exercise 3.1 Official Answer
# Weight on Earth / Moon after 10 years.  Each year increase 0.5kg

weight = eval(input("Please enter current weight (kg): "))
wei10ear = 0.5 * 10 + weight
wei10moo = wei10ear * 0.165
print("After 10 years, your weight on Earth is {:.2f} kg".format(wei10ear))
print("On Moon is {:.2f} kg".format(wei10moo))
