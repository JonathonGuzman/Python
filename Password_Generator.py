
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Chosen characters will be added to the variable
variable = []

# Amount of characters chosen will be added to variable
for letter_int in range(0, nr_letters, +1):
  variable.append(random.choice(letters))

for symbol_int in range(0, nr_symbols, +1):
 variable.append(random.choice(symbols))

for number_int in range(0, nr_numbers, +1):
  variable.append(random.choice(numbers))

# Will shuffle all chosen character
random.shuffle(variable)

# Connects all characters
password = ''.join(variable)

print(f"Here is your password: {password}")

