import random
from collections import Counter


def number_guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("\nCongratulations!")
                print("You guessed the correct number.")
                print("Attempts:", attempts)

                if attempts <= 5:
                    print("Score: Excellent!")
                elif attempts <= 10:
                    print("Score: Good!")
                else:
                    print("Score: Keep practicing!")

                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def word_counter():
    print("\n===== WORD COUNTER =====")

    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.lower().split()
        word_frequency = Counter(words)

        print("\nTotal words:", len(words))
        print("\nWord Frequency:")

        for word, count in word_frequency.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found!")
        print("Please check the file name and try again.")


def main():
    while True:
        print("\n==============================")
        print(" NUMBER GUESSING & WORD COUNTER")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


main()