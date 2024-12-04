
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill? "))

# Calculate the total bill including the tip
TotalBill = bill+(tip/100)*bill
# Calculate how much each person should pay and round to 2 decimal places
print(f"Each person should pay: ${round(TotalBill/people,2)}")
