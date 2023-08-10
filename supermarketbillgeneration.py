from datetime import datetime

name = input("Enter your name: ")

# Dictionary of items with their prices
items = {
    "Rice": 50,
    "sugar": 20,
    "oil": 200,
    "salt": 20,
    "paneer": 60,
    "maggie": 70,
    "mangoes": 100,
    "ata": 90,
    "maida": 67,
    "dal": 110
}

pricelist = []
totalprice = 0

print("List of items:")
for item, price in items.items():
    print(f"{item} - Rs {price}/kg")

while True:
    item = input("Enter the item you want to buy (or 'exit' to finish): ")
    if item.lower() == "exit":
        break

    if item in items:
        quantity = float(input(f"Enter the quantity in kg for {item}: "))
        price = items[item] * quantity
        pricelist.append((item, quantity, price))
        totalprice += price
    else:
        print("Item not found in the list. Please enter a valid item.")

# Print the bill
print("\n\n===== Supermarket Bill =====")
print(f"Date: {datetime.now():%Y-%m-%d %H:%M:%S}")
print(f"Customer Name: {name}")
print("---------------------------")
for item, quantity, price in pricelist:
    print(f"{item} - {quantity:.2f} kg - Rs {price:.2f}")
print("---------------------------")
print(f"Total: Rs {totalprice:.2f}")
print("===========================")
