import random

# Step 1: Word list
words = ["apple", "table", "chair", "light", "plant"]
word = random.choice(words)
word_letters = list(word)
guessed = ['_'] * len(word)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")

# Step 2: Game loop
while attempts > 0 and '_' in guessed:
    print("\nWord: ", ' '.join(guessed))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")
    
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        for i, letter in enumerate(word_letters):
            if letter == guess:
                guessed[i] = guess
        print("✅ Good guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess.")

# Step 3: Game Over
if '_' not in guessed:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n💀 Game over! The word was:", word)
