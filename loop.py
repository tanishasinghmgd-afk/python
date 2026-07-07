n = int(input("enter the number you want the square of: "))
exp = int(input("enter the exponent(power): "))

#initialization
result = 1

for i in range(exp):
    result = result*n

    print(f"{n} to the power {exp} is {result}")

