#Activity 1
#Let's check the datatype of different values
"""a=5
print("type of a:", type(a))

b = 2.5
print("type of b:", type(b))

c = "coding"
print("type of c:", type(c))

d = True
print("typeof d:", type(d))"""


#Activity 2 
#Assigning different variables
name = "Penguin"
age = 15
is_student = True
weight = 38.5

#Printing different variables and their data type
print("Name :", name)
print("Data Type of Name is", type(name))

print("Age:", age)
print("Data type of age is", type(age))

print("is_student:", is_student)
print("Data type of is_student is ", type(is_student))

print("weight:",weight)
print("data type of weight is", type(weight))

#Type casting to convert the data type of variables
print("\n After type casting..")
age = str(age)
print(age)

print("Data type of age is", type(age))

weight = int(weight)
print(weight)
print("data type of weight is", type(weight))

#Activity 3

text = str(input("Enter a string:"))
revText = text[::-1]
text = revText

print("Reverse of give string is:")
print(text)



