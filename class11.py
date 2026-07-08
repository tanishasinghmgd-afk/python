i = 0
while i < 10:
    print(i)
    i += 2
    
#activity 1

n = int(input("enter the value of terms: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
    print("\nSum =", sum)

#activity 2
num = int(input("enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")

#activity 3
#while True:
    #print("I WILL RUN FOREVER")
     
i = 10
while i >= 1:
    print(i)
    i -= 1 


  


