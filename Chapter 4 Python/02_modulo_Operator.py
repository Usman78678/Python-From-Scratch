# Modulo Operator Example
# This program checks if a number is even or odd using the modulo operator.

number = int(input("Enter the number: ")) # Taking input from the user
if number % 2 == 0: # Using modulo operator to check for evenness
    print("this number is Even") # If the remainder is 0, it's even
else: 
    print("this number is odd")   # If the remainder is not 0, it's odd