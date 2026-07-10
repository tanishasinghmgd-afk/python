#activity 1
"""print("half pyramid pattern of stars(*): ")
n = int(input("enter th number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#activity 2
rows = int(input("please enter the total number of rows: "))
number = 1
print("floyd's tirangle")
for i in range(1,rows + 1):
    for j in range(1,i + 1):
        print(number, end = " ")
        number = number + 2 
    print()"""      

#activity 3
row = int(input("enter the number of rows: "))

for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2*i + 1):
        print("*", end="")
    print()
for i in range(row - 2, -1, -1):
    for j in range(row - i - 1):
        print(" ", end="")         
    for j in range(2*i + 1):
        print("*", end="")
    print()
    
               


    
