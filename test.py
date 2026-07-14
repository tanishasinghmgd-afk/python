"""a = 15
b = 5
avg = (a + b)/2
print("average:",avg)

password = input("enter password: ")
if not password == "python123":
    print("access granted")
else:
    print("not  granted")   

total = 0
i = 1
while i<=5:
    total = i
    i += 1
    print("sum:",total)"""

guess = int(input("enter your guess: "))
secret_numb = 20
attempts_left = 5

print("you have 5 attempts to guess the number!")

while attempts_left > 0:
    print(f"attempts left:{ attempts_left}")
if guess == secret_numb:
    print("you guessed the number {secret_numb} correctly! ")


attempts_left -= 1
if attempts_left > 0:
    difference = (secret_numb - guess)
 
