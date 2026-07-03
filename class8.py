#activity 1

v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print("value of (v+w)* x/y is", z)

name = "alex"
age = 0
if name == "alex" or name == "jhon" and age >= 2:
    print("hello welcome")
else:
    print("good bye")


#activity 2

numn = int(input("enter the number: "))
numd = int(input("enter a number: "))

if numn%numd==0:
    print("\n" +str(numn)+ "is divisible by" +str(numd))

else:
    print("\n" +str(numn)+ "is not divisible by" +str(numd))



#activity 3

count = 40
mean = 38
incorrect_num = 36
correct_num = 56    

correct_sum = count*mean - incorrect_num + correct_num

correct_mean = correct_sum/count

print(correct_mean)

#activity 4
a = int(input("enter a value:"))
b = int(input("enter a value: "))
c = int(input("enter a value: "))

avg = (a + b + c)/3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print(f"{avg} is higher than {a},{b},and{c}")
elif avg > a and avg > b:
    print(f"{avg} is higher than {a},and{b}") 
elif avg > a and avg > c:
    print(f"{avg} is higher than {a}, and {c}")
elif avg > b and avg > c:
    print(f"{avg} is higher than {b}, and {c}")
elif avg > a:
    print(f"{avg} is higher than {a}")
elif avg > b:
    print(f"{avg} is higher than {b}") 
elif avg > c:
    print(f"{avg} is higher than {c}")
else:
    print("invalid input") 
                       