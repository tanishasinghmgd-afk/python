def total_bill(bill_amount,tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"please pay ${total}")
    return total

total_bill(150,20)

def seating_arrangements(guests):
    '''this is a recursive function to find the number of seating arrangements for guests'''
    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * seating_arrangements(guests - 1)
    
print(seating_arrangements.__doc__)

print("seating arrengements for 1 guest:",seating_arrangements(1))

print("seating arrengements for 2 guest:",seating_arrangements(2))

print("seating arrengements for 3 guest:",seating_arrangements(3))

print("seating arrengements for 5 guest:",seating_arrangements(5))
