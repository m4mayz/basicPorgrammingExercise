# Array of Products
products = [
    "Hat",
    "Shoes"
]

def display():
    print("\nList of Products:")
    print("ID | Name")
    for n, i in enumerate(products):
        print(f"{n}    {i}")

while True:
    print("\nSelect menu:\n1. Add new item.\n2. Delete product by name.\n3. Delete product by ID\n4. Show products list.\n5. Exit program.\n")
    menu = input("Enter your choice > ")
    if menu == '1':
        addItem = input("\nEnter your product name: ")
        products.append(addItem)
        print(f"Product named ({addItem}) added successfully!")
        display()
    elif menu == '2':
        display()
        removeName = input("\nEnter the product name you want to remove: ")
        if removeName in products:
            products.remove(removeName)
            print(f"Product named ({removeName}) removed.")
        else:
            print(f"Error. Product named ({removeName}) is not exist.")
    elif menu == '3':
        display()
        removeID = input("\nEnter the product ID you want to remove: ")
        if (int(removeID)) < len(products):
            products.pop(int(removeID))
            print(f"Product with ID ({removeID}) removed.")
        else:
            print(f"Error. Product with ID ({removeID}) is not exist.")
    elif menu == '4':
        display()
    elif menu == '5':
        print("\nBye bye, have a nice day! :)")
        break
        exit()
    else:
        print("\nInvalid input!")