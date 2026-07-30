import random

def get_word():
    words = ["python", "hangman", "programming", "developer", "keyboard"]
    return random.choice(words).upper()

def display_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    word = get_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("=" * 40)
    print("Welcome to Hangman")
    print("=" * 40)
    print(f"\nThe word has {len(word)} letters.")
    print("You have 6 incorrect guesses allowed.\n")

    while incorrect_guesses < max_incorrect:
        print(f"Word: {display_state(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("\nGuess a letter: ").upper().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")

    print(f"\nGame Over! The word was: {word}")


def main():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        play_hangman()
        play_again = input("\nPlay again? (yes/no): ")
    print("\nThanks for playing.")


if __name__ == "__main__":
    main()
