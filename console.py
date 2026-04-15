# Smart Shop Billing System

products = {
    1: ("Apple", 10),
    2: ("Banana", 5),
    3: ("Milk", 50),
    4: ("Bread", 40)
}

total = 0

print("============================")
print("   Welcome to Smart Shop   ")
print("============================")

while True:
    print("\n--- Product Menu ---")
    for key, (name, price) in products.items():
        print(f"{key}. {name} - {price} tk")
    print("5. Exit")

    choice = int(input("\nEnter choice: "))

    if choice == 5:
        break

    if choice not in products:
        print("❌ Invalid choice! Try again.")
        continue

    quantity = int(input("Enter quantity: "))

    name, price = products[choice]
    subtotal = price * quantity
    total += subtotal
    print(f"✅ Added: {name} x{quantity} = {subtotal} tk")

print("\n============================")
print(f"   Total Bill: {total} tk")
print("   Thank you! Come again!  ")
print("============================")