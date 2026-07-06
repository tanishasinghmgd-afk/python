grade = int(input("enter your class: "))

if grade == 10:
    print("enter the age of the student: ")

    age = int(input("enter your age: "))

    if( age > 10 and age < 20):
        print("you are allowed in the class")
    else:
        print("you are not allowed in the class")
else:
    print("you are not in grade 10")             