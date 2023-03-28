
def read_words(filename):
 with open(filename, 'r') as file:
 words = file.read().splitlines()
 return words

import random
def random_word(words):
 return random.choice(words)

def hangman(word):
 print("Welcome to Hangman!")
 guesses = []
 turns = 6
 while turns > 0:
 failed = 0
 for char in word:
 if char in guesses:
 print(char, end=' ')
 else:
 print("_", end=' ')
 failed += 1
 if failed == 0:
 print("\nYou win!")
 break
 guess = input("\nGuess a letter: ").lower()
 if guess in guesses:
 print("You already guessed that letter!")
 elif guess in word:
 guesses.append(guess)
 else:
 turns -= 1
 print("Incorrect! You have", turns, "guesses left.")
 if turns == 0:
 print("\nYou lose! The word was", word)
if __name__ == '__main__':
 words = read_words('words.txt')
 while True:
 word = random_word(words)
 hangman(word)
 play_again = input("Do you want to play again? (y/n) ").lower()
 if play_again != 'y':
 break
