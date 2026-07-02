#activity 1
"""x = 5
if(type(x)is int):
    print("true")
else:
    print("false")
    
x = 5.5
if(type(x) is not float):
    print("true")  
else:
    print("false")

x = 20
y = 20
if (x is y):
    print("x&y same identity")

y = 30
if(x is not y):
    print("x&y have different identity")"""

#activity 3
print("enter marks obtained in 5 subjects: ")

markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

total = markone + marktwo + markthree + markfour + markfive
avg = int(total/5)

validrange = range(0, 101)

if avg not in validrange:
    print("invalid range")
elif avg in range(91, 101):
    print("your grade is A1")
elif avg in range(81, 91):
    print("your grade is A2")
elif avg in range(71, 81):
    print("your grade is B1")
elif avg in range(61, 71):
    print("your grade is B2")
elif avg in range(51, 61):
    print("your grade is C1")
elif avg in range(41, 51):
    print("your grade is C2")
elif avg in range(33, 41):
    print("your grade is D")

                            