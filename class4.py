#storing values
"""tree1 = int(input("enter the value of tree1: "))
tree2 = int(input("enter the value of tree2: "))
tree3 = int(input("enter the value of tree3: "))
tree4 = int(input("enter the value of tree4: "))
tree5 = int(input("enter the value of tree5: "))

#finding the total sum of trees
sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all the 5 trees is:", sum)

#finding the average of trees
average = sum/5
print("the average of all the trees is:", average)"""

#activity 2
#taking total amount as input from user
amount = int(input("please enter amount for withdraw :"))

#calculating the number of notes of different denominations
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("notes of 100 rupee", note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)

#activity 3
#take marks as input from user
print("enter marks obtained in 4 subjects")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

#lets calculate the percentage of marks
sum = math+english+science+hindi 
print("sum of math,english,science,hindi = " ,sum)


perc = (sum/400)*100

print(end = "percentage mark =")
print(perc)

