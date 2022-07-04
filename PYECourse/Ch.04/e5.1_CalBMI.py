# Ch.04.3 BMI calculation
# BMI = weight(KG) / height(CM)^2

weight, height = eval(input("Please Enter weight(KG) and height(CM), divide by ',': "))

bmi = weight / pow((height / 100), 2)

print("BMI: {:.2f}".format(bmi))

who, dom = "", ""

if bmi < 18.5:
    who = "Thin"
elif bmi < 25:
    who = "Normal"
elif bmi < 30:
    who = "Fat"
else:
    who = "Obesity"

if bmi < 18.5:
    dom = "Thin"
elif bmi < 24:
    dom = "Normal"
elif bmi < 28:
    dom = "Fat"
else:
    dom = "Obesity"

print("BMI by WHO: {}, DOM: {}".format(who, dom))
