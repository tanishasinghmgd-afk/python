num = 152026
count = 0

original_num = num
if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num = num // 10
        print(f"the number of digits in {original_num} is: {count}")  
