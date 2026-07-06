#activity 1

"""medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

if medical_cause == 'Y':
    print("you are allowed.")
else:
    atten = int(input("Enter the attendance of the student: "))

    if atten >= 75:
        print("allowed")
    else:
        print("not allowed")

#activity 2
units = int(input("please enter the number of units you consumed: "))

if(units < 50):
    amount = units * 2.60
    surcharge = 25

elif(units <= 100):
    amount = 130 + ((units - 50)* 3.25)
    surcharge = 35

elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45 

else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\n Electricity Bill =" , total)"""

#activity 3
print("select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("enter your choice: "))

if( choice == 1):
    print("what type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2 = int(input("enter your choice 2: "))

    if choice2 == 1:
        print("you have selected scooter")
    else:
        print("you have slected scooter")

elif( choice == 2):
    print("what type of car? ") 
    print("1. Sedan")
    print("2. XUV")
    choice3 = int(input("enter your choice3: "))

    if choice3 == 1:
        print("you have selected sedan.")
    else:
        print("you have selected XUV")

else:
    print("wrong choice") 


     