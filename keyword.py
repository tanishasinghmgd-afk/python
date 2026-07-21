def calculate_change(paid,price): 
    change = paid - price
    return change

ticket_price = 30
print("====PARKING TICKET PAYMENT HELPER====")
print(f"this paring ticket costs {ticket_price} units.")
print("accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("insert a coin(1,5,10,25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("invalid coin, try again!\n")
        continue

    total_inserted += coin 
    coins_inserted += 1
    print(f"inserted {coin}. total so far: {total_inserted}\n")

    if total_inserted >= ticket_price:
        print("enought money inserted!\n")
        break

change_due = calculate_change(total_inserted,ticket_price)
print("printing your parking ticket....")

if change_due == 0:
    pass
else:
    print(f"here is your change: { change_due} units.")

print("\n=====PAYMENT SUMMARY=====")
print("ticket price: ",ticket_price)
print("coins inserted: ",coins_inserted)
print("total paid: ",total_inserted)
print("change given: ",change_due)
print("=============================")
print("praking ticket payment complete!!")
