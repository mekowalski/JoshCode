def bmiCalculator(weight, height):
    bmi = (weight / (height * height)) * 703
    return bmi

def bmiResult(weight, height):
    calculate = bmiCalculator(weight, height)
    if calculate <= 18.5:
        print("Underweight")
    elif calculate > 18.5 and calculate <= 25:
        print("Normal")
    else:
        print("Overweight")
    
weight = int(input("Enter weight(lbs): "))
height = int(input("Enter height(in): "))
bmiResult(weight, height)
