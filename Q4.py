SET_OF_ITEMS = set()
PRICES = {}
lst = []
for i in range(1, 6):
    item_name = input(f"Name of item {i}: ")
    SET_OF_ITEMS.add(item_name)
    print(SET_OF_ITEMS)
    x = SET_OF_ITEMS.pop()
    print("Enter price for", x)
    PRICES[x] = int(input(f"Enter price for {x}: "))
amount = sum(PRICES.values())
print("\n*_*_*_*_* BILL *_*_*_*_*")
print("{:<15}{:<15}".format("SET_OF_ITEMS", "PRICES"))
for item, price in PRICES.items():
    print("{:<15}{:<15}".format(item, price))
print("Total Amount = Rs.", amount)
print("Maximum Price =", max(PRICES.values()))
print("Minimum Price =", min(PRICES.values()))
print("\nTHANKS FOR VISITING")

