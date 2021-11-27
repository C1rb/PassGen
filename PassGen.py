#PassGen

print("PassGen Version 1.2")

import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdeghijklmnopqrstuvwxyz"
num = "0123456789"
sym = "!()[]{}"

list1 = []

while True:
    element = str(input(" Enter any key to start the program :"))
    list1.append(element)
    choice = input("Enter y to generate a new password and c to close the program :")
    if choice == "y":
        all = upper + lower + num + sym
        length = 9 
        password = "" .join(random.sample(all, length))
        print(" The password generated is :", password)
    elif choice == "c":
        print("Closing Program")
        break;
        
    else:
        print("Please enter y or c only")   
