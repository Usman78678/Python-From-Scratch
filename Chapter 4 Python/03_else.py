# Nested if/else Example
# This program determines if a user can ride a roller coaster based on height and age.

print("Welcome to Adventure Island")
height = float(input("Enter Your Height in CM :")) # Taking height input from the user
if height > 120:
    print("You can ride the roller coaster")
    age = int(input("Enter your age in years:")) # Taking age input from the user
    if age <=18: # Nested if condition to check age
        print("you need to pay $7 for the ticket") # If age is 18 or below
    else:
        print("you need to pay $12 for the ticket") # If age is above 18
else:
    print("you cannot ride the roller coaster")    # If height is 120 cm or below    
    