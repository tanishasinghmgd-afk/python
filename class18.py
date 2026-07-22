#activity 1

"""try:
    number = int(input("enter a number: "))
    print("the number entered is", number)
except ValueError as ex:
    print("exception: ",ex)

#activity 2

try:
    num1,num2 = eval(input("enter two numbers,separated by a comma: "))
    result = num1/num2
    print("result is: ",result)

except ZeroDivisionError:
    print("division by zero is error!")
except SyntaxError:
    print("comma is missing enter numbers seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")


#activity 3

valid = False
while not valid:
    try:
        n = int(input("enter a number: "))
        while n%2 == 0:
            print("bye")
        valid = True
    except ValueError:
        print("invalid")"""


try:
    user_input = input("enter the withdrawl amount: ")
    amount = float(user_input)
    print(f"amount withdrawn: {amount}")
except ValueError:
    print("invalid amount entered")


    
