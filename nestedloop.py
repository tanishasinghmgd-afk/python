print("===INVENTORY STOCK COUNTER===")
print("counting stock for products one at a time")

box_sizes = [50,20,10,5,1]
products_counted = 0
total_items = 0
log = [] #stores each product's box breakdown for the final reprot

#outer while loop - runs once per product
counting = True
while counting:
    product_name = input("enter product name: ")
    quantity = int(input(f"enter total quantity for {product_name}: "))

    if quantity <= 0:
        print("invalid quantity. please enter a positive number.")
        continue
    print(f"packing {quantity} items of {product_name:}")
    print("-" * 30)

    remaining = quantity
    i = 0
    used = {}
#inner while loop - breaks quantity into box sizes
    while i < len(box_sizes):
        count = remaining // box_sizes[i]
        if count > 0:
            print(f"{count} box(es) of {box_sizes[i]} items = {count * box_sizes[i]}")
            
            used[box_sizes[i]] = count
            remaining -= count * box_sizes[i]
        i += 1
    products_counted += 1
    total_items += quantity
    log.append({"product": product_name, "used": used})        
    print(f"stock counted successfully for {product_name}")

    again = input("add another product?(yes/no): ").strip().lower()
    if again != "yes":
        counting = False
print("===FINAL BOX SIZE REPORT===")
for box in box_sizes:
    total_boxes = 0

    #innerinner for loop - checks every product's ugade of this box size
    for entry in log:
        total_boxes += entry["used"].get(box, 0)
    if total_boxes > 0:
        print(f"{box} - item boxes used todal : {total_boxes}")
print(f"products counted : {products_counted}")
print(f"total items: {total_items}") 
print("inventory counting complete!")





