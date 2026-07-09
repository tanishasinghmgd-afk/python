"""i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(j, end = " ")
        j = j + 1
    print()
    i = i + 1

for i in range(1,6):
    for j in range(1,11):
        print(j, end = " ")
    print()

#activity 1

string = input("please enter your word: ")
char = input("please enter your own character: ")

i = 0
count = 0
while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1
print("the total number of times", char, "has occured =", count)"""

#activity 2

lower = int(input("enter a lower range: "))
upper = int(input("etner a upper range: "))

print("prime numbers between", lower, "and", upper, "are: ")

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#activity 3
num = int(input(""))