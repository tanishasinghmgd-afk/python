def greet_customer():
    print("welcome to the art supplies store!")
    print("get your colours,brushes,and paper here.")

greet_customer()

price_per_item = float(input("enter the price per art itmes bought: "))
items_bought = int(input("enter the number of art items bought: "))

def calculate_total(price, items):
    total = price * items
    return total

total_cost = calculate_total(price_per_item,items_bought)
rounded_total = round(total_cost, 2)
print("total cost: ", rounded_total)


amount_paid = float(input("enter the amount paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(items):
    if items >= 5:
        return "great choice! you picked many art suplies for your project"
    else:
        return "thanks for shopping at the art supplies store!"
    
closing_message = thank_you_message(items_bought)  

print("")
print('===ART SUPPLIES BILL===')
print("price per item:", price_per_item)
print("items bought:", items_bought)
print("total cost:", rounded_total)
print("amount paid", amount_paid)
print("change due", rounded_change)
print(closing_message)

print("=========================================================")

