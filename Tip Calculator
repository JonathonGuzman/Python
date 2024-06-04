print("Welcome to the Tip Calculator")

# Easy access to values with names given. And floats allow decimal points.
bill = float(input("What was the bill total? $"))

# Int turns inputs to whole numbers.
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

bill_with_tip = ((bill * (tip / 100)) + bill)

split_bill = (bill_with_tip / people)

# Rounds the final number to two decimal points.
final_amount = "{:.2f}".format(split_bill)

print(f'Each person should pay ${final_amount}.')
