#input
print("Please, enter your weight in kg")
weight = float(input())
print("Please, enter your height in cm")
height = float(input())

#function
def bmi_calculate(weight, height):
    height = height / 100
    return weight / (height * height)

#BMI calculation
if(weight <= 0 or height <= 0):
    print("Error: height must be a positive number")
else:
    result = round(bmi_calculate(weight, height), 2)

    print("You BMI is", result)

    if result < 18.5:
        print("Underweight")
    elif result >= 18.5 and result < 25:
        print("Normal weight")
    elif result >= 25 and result < 30:
        print("Overweight")
    elif result >= 30:
        print("Obesity")

