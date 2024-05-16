# I've added a list of possible words that are randomly selected
# I've made sure to only count the attempt to the final score if it is a valid one (if it isn't a valid attempt the loop restarts without incrementing the attempts couunter)

import random

words = {
    1: "hope",
    2: "tree",
    3: "blue",
    4: "apple",
    5: "grape",
    6: "orange",
    7: "banana",
    8: "elephant",
    9: "cheetah",
    10: "rhinoceros"
}

def generate_first_hint(secret_word):
    return "_ " * len(secret_word)

def generate_hint(secret_word, guess):
  
  hint = []
  for i in range(len(secret_word)):
    if guess[i] == secret_word[i]:
      hint.append(guess[i].upper())
    elif guess[i] in secret_word:
      hint.append(guess[i].lower())
    else:
      hint.append("_")
  
  return " ".join(hint)

def main():
  print("Welcome to Letter Logic!")
  
  attempts = 0
  
  word_key = random.choice(list(words.keys()))
  secret_word = words[word_key]
  hint = generate_first_hint(secret_word)
  
  while "".join(hint.split()).lower() != secret_word:
    print("your hint is: " + hint)
    print(f"rememeber to insert a word with {len(secret_word)} letters")

    guess = input("What is your guess ? ")
    
    if len(guess) != len(secret_word):
      print("Sorry, the guess must have the same number of letters as the secret word.")
      attempts += 1
      continue
    
    hint = generate_hint(secret_word, guess)
    attempts += 1

  print("Congratulations! You guessed the word !")
  if attempts == 1:
    print("It took you 1 guess")
    return
  print(f"It took you {attempts} guesses.")

main()

