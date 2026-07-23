#activity 1
"""import random
playing = True
number = (random.randint(0,9))
#print("computer guess: ",number)
print("i will generate a number from 0 to 9,and yoy have to guess the number one digit at a time.")

print("the game ends when u get 1 hero!")

while playing:
    guess = int(input("give me your best guess!\n"))
    if number == guess:
        print("you win thr game")
        print("the number was: ",number)
        break
    else:
        print("your guess isin't quite right,try again.\n")


#activity 2
import random
while True:
    user_action = input("enter a choice(rock,paper,scissors): ")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"both players selected{user_action}.it is a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
           print("rock smashes scissors! you win!")
        else:
            print("paper covers rock! you lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! you win!")
        else:
            print("scissors cuts paper! you lose.")  
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper! you win!")
        else:
            print("rock smashes scissors! you lose.") 
    play_again = input("play again?(y/n): ")
    if play_again != "y":
        break"""                             

#activit 3
import math
print('the floor and celeing value of 23.56 are: ' + str(math.ceil(23.56)) + ',' + str(math.floor(23.56)))

x = 10
y = -15
print('the value of x after copying the sign from y is: ' + str(math.copysign(x,y)))

print('the value of -96 and 56 are: ' + str(math.fabs(-96)) + ',' + str(math.fabs(56)))

print('the GCD of 24 and 56: ' + str(math.gcd(24,56)))