
# Graphics is a seperate folder
import random
import graphics

# Gives graphics a name
rock = graphics.rock
paper = graphics.paper
scissors = graphics.scissors

# List for the input.
integer = [0, 1, 2]

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
# or use images as list [rock, paper, scissors]
# print(graphics[choice])

# Computer chooses random integer
random_choice = random.randint(0, 2)
# print(f"Computer chose:")

# If user puts a invalid number. Must be checked first/
if choice not in integer:
  print("Invalid number, you lose")

# User choice will give the following command.
if choice == 0:
  print(rock)
  if random_choice == 0:
    print(rock + "\nDraw")
  elif random_choice == 1:
    print(paper + "\nYou lose")
  else:
    print(scissors + "\nYou win")

if choice == 1:
  print(paper)
  if random_choice == 1:
    print(paper + "\nDraw")
  elif random_choice == 2:
    print(scissors + "\nYou lose")
  else:
    print(rock + "\nYou win")

if choice == 2:
  print(scissors)
  if random_choice == 2:
    print(scissors + "\nDraw")
  elif random_choice == 0:
    print(rock + "\nYou lose")
  else:
    print(paper + "\nYou win")


