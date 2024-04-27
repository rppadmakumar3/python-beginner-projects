import random

words = ["python", "elephant", "peacock"]

chosen_word = random.choice(words)
word_display = ["_" for _ in chosen_word]
attempts = 10

print("Welcome to Hangman!")

while attempts>0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess the Letter : ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Give Correct Letter!!!")
        attempts -= 1

if '_' not in word_display:
    print("You Guess all words")
    print(" ".join(word_display))
else:
    print("You Lost!")