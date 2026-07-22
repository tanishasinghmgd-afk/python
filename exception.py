try:
    age = int(input("enter your age: "))    
    if age % 2 == 0:
        print("the entered age is even")
    else:
        print("the entered age is odd")
except ValueError:
    print("value error,please enter a valid integer for age")

        
