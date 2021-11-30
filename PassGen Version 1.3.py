#PassGen

print("PassGen Version 1.3")

#Imports and character types
import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
sym = "!()[]{}"

#Main Code(loop, password generation, errors and answer checking)
list1 = []

while True:
    element = str(input(" Enter any key to start the program :"))
    list1.append(element)
    choice = input(" Enter y to generate a new password and c to close the program :")
    if choice == "y":
        all = upper + lower + num + sym
        length = 9
        password = "" .join(random.sample(all, length))
        print(" The password generated is :" ,password)
        print("---------------------------------------------------------------------------------------")
    elif choice == "c":
        print("Closing Program")
        break;
                
    else: 
        print("Please enter y or c only.")   
