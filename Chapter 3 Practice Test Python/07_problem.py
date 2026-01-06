# Calculate the total bill per person including tip

bill = float(input("Enter the Total Bill Amount: ") ) #convert string input to float
a = int(input("How many tip percentage you want to give? 10, 12 or 15: ") ) #convert string input to integer
b = int(input("In how many people you want to split the bill: ") ) #convert string input to integer
per_person_bill = (bill + (bill * a / 100))/b # calculate total bill per person including tip
print("the total bill for per person is :", per_person_bill) #print the total bill per person including tip