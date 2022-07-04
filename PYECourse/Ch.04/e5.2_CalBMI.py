# Ch.04.3 BMI calculation
# BMI = weight(KG) / height(CM)^2

weight, height = eval(input("Please Enter weight(KG) and height(CM), divide by ',': "))

bmi = weight / pow((height / 100), 2)

print("BMI: {:.2f}".format(bmi))

who, dom = "", ""

if bmi < 18.5:
    who, dom = "Thin", "Thin"
elif 18.5 <= bmi < 24:
    who, dom = "Normal", "Normal"
elif 24 <= bmi < 25:
    who, dom = "Normal", "Fat"
elif 25 <= bmi < 28:
    who, dom = "Fat", "Fat"
elif 28 <= bmi < 30:
    who, dom = "Fat", "Obesity"
else:
    who, dom = "Obesity", "Obesity"

print("BMI by WHO: {}, DOM: {}".format(who, dom))
