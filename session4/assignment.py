# Siti wants to sell cosmetic items online.
# She got several cosmetic items from suppliers with various variants and different prices.
# Siti wants to sell the item at a price of 10 percent of what she bought
# from the supplier and wants to know the price. 
# Make a simple application for the problem.

while True:
    try:
        print('==============================')
        print('Price of 10 percent Calculator')
        print('==============================')
        
        realPrice = float(input("Enter the price: \t\t: Rp. "))
        price = realPrice + (realPrice * 0.10)
        
        print(f"The price to sell is \t\t: Rp. {int(price):,}")
        print()
        break
    
    except ValueError:
        print('The input is wrong! please input number.')