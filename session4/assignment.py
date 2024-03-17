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
        
        realPrice = float(input("Enter the price: "))
        price = realPrice + (realPrice * 0.10)
        
        print(f"The price to sell is: Rp. {price}")
        break
    
    except ValueError:
        print('The input is wrong! please input number only.')