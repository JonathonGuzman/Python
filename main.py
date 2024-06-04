import random
import hangman_pics
import hangman_words
from replit import clear

random_word = random.choice(hangman_words.word_list)

print(hangman_pics.logo)

# Keeps track of wrong guesses
live = 6

# Gives '_' according to characters in words
display = ["_"] * len(random_word)

# placement is the amount in the random word. variable runs through letters contained in the word. enumerate counts the random word and starts with 1 instead of 0. ex. 1-c, 2-a, 3-m, e-4, l-5
while "_"  in display:
  guess = input("Guess a letter: ").lower()
  
  clear()

  if guess in display:
    print(f"You have already guessed {guess}")
  
  if guess in random_word:
    for placement, variable in enumerate(random_word):
      if guess == variable:
        display[placement] = guess
  print(" ".join(display))

  if guess not in display:
    print(f"{guess} is not in the word guess again.")
    live -= 1

  if live == 0:
    print(f"You Lose. Word was {random_word}.")
    break
  
  if "_" not in display:
    print("You win.")

  print(hangman_pics.stages[live])