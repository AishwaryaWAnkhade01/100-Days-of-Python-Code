#BMI Calculator
print('Welcome to the BMI Calculator!!!')
height=float(input('Enter your height'))
weight=int(input('ENter your weight'))
bmi=weight/(height**2)
print(f'Your BMI is {bmi:.2f}')

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")