"""This is the day2 of the python programming couse in which have to calculate the tip and how much each person should pay including the tip"""

print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

total_bill += tip / 100 * total_bill
total_bill /= number_of_people

print(f"Each person should pay: ${round(total_bill, 2)}")