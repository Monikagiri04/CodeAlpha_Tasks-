import random

# List of words
words = ["python", "internship", "hangman", "computer", "programming"]

word = random.choice(words)

# Create blank display
guessed_word = ["_"] * len(word)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
