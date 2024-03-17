# from the previous application (session 4), Siti wants to be able to make transactions 
# in the application directly when there is a purchase.
# the application can display the name of the item price and available stock.
# at the end it will be seen how many transactions and profits
# make a simple application for the problem

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Store:
    def __init__(self):
        self.items = []
        self.transactions = 0
        self.profit = 0

    def add_item(self, name, price, stock):
        self.items.append(Item(name, price, stock))

    def sell_item(self, option):
        if option > 0 and option <= len(self.items):
            item = self.items[option - 1]
            if item.stock > 0:
                item.stock -= 1
                self.transactions += 1
                self.profit += item.price * 0.10
                print()
                print(f"Selling {item.name} for Rp. {float(item.price + (item.price * 0.10))}. Remaining stock: {item.stock}")
            else:
                print()
                print(f"Sorry, {item.name} is out of stock.")
        else:
            print(f"Invalid option. Please try again.")

    def report(self):
        print("=============================")
        print(f"Total transactions: {self.transactions}")
        print(f"Total profit: Rp.{float(self.profit)}")
        print()

    def print_items(self):
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name} - Price: Rp.{item.price + (item.price * 0.10)}, Stock: {item.stock}")

# Create a store
store = Store()

# Add some items
store.add_item("Lipstick", 100000, 10)
store.add_item("Mascara", 150000, 4)
store.add_item("Foundation", 200000, 5)
store.add_item("Eyeliner", 50000, 10)
store.add_item("Blush", 120000, 7)

while True:
    print()
    print("List of cosmetics (price is within 10% of the original price): ")
    store.print_items()
    print("===============================================================")
    print("Menu:")
    print("1. Sell item")
    print("2. Report")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("=============================")
        option = int(input("Enter the option of the item to sell: "))
        store.sell_item(option)
        store.report()
    elif choice == '2':
        store.report()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
