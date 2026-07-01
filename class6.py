#activity 3

"""height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))

BMI = weight/(height/100)**2

print("your BMI is", BMI)

if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 25:
    print("you are healthy")
elif BMI <= 30:
    print("you are overweight")
elif BMI <= 35:
    print("you are severly over weight")
elif BMI <= 40:
    print("you are obese") 

else:
    print("you are severly obese.")"""

#activity 1

"""a = 10
b = 12
c = 0

if a and b and c:
    print("all the numbers have boolean value as true")
else:
    print("at least one number has boolean value as false")


a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("either of the number is greater than 0")

else:
    print("no number is greater than 0")

if b > 0 or c > 0:
    print("either of the number is greater than 0")

else:
    print("no number is greater than 0")"""


#activity 2

a = 10
b = 12
c = 12

#print(not(a == b))

#print(not(b == c))

a = "python"
b = "coding"

if not (a == b):
    print("both are equal")
else: 
    print("both are not equal")

a = 4
b = 5
if not ((a==4)==(b==5)):
    print("given conditions are true")
else:
    print("given conditions are false")


a = int(input("enter a number:"))
if not (a % 2 == 0):
    print(a, "is an odd number.")
else:
    print(a, "is an even number.")

