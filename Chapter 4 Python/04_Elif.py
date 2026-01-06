# Roller Coaster Ticketing System
# This program determines if a user can ride a roller coaster based on their height and age, and calculates the ticket price accordingly.

print("Welcome to Adventure Island")
height = int(input("Enter your height in CM:"))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("you need to pay $5 for the ticket")
    elif age <=18:
        print("You need to pay $7 for the ticket")
    else:
        print("you need to pay $12 for the ticket")
        
else:
    print("you cannot ride the roller coaster")    
