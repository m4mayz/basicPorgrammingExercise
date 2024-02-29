#Write a program that compares two integers and prints whether they are equal, greater, or smaller.

#loop
while True:
    try:
        #let user input number
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))
        
        if (x == y):
        #if the first number and second number are equal
            print(f"{x} and {y} are equal.")
        elif (x > y):
        #if the first number is greater than second number
            print(f"{x} is greater than {y}.")
        elif (x < y):
        #if the second number is greater than first number
            print(f"{y} is greater than {x}.")
        
        #stop looping
        break
    
    #if the input is not integer, show wrong input message and loop back to the input
    except ValueError:
        print("The input is wrong, please input an integer value.")