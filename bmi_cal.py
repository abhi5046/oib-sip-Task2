weight=float(input("Enter your correct weight in kg:"))
height=float(input("Enter your correct height in meater:"))

bmi= weight/(height)**2

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")
