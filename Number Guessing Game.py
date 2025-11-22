# -------------------------------
# Project 2 : Number Guessing Game
# Author    : Muhammad Saeed
# Internship: Syntecxhub - Python Programming Internship
# Description: A number guessing game with difficulty levels .
# -------------------------------

import random

# Function to choose difficulty level
def choose_difficulty():
    print(" Choose difficulty level : ")
    print(" 1. Easy (1 - 10) ")
    print(" 2. Medium (1 - 50) ")
    print(" 3. Hard (1 - 100) ")

    choice = input(" Enter choice (1-3) : ")

    if choice == "1":
        return 1, 10
    elif choice == "2":
        return 1, 50
    elif choice == "3":
        return 1, 100
    else:
        print("Invalid choice! Defaulting to Easy.")
        return 1, 10

# Main guessing game function
def guessing_game():
    best_attempt = None

    while True:
        low, high = choose_difficulty()
        secret_number = random.randint(low, high)
        attempts = 0

        print(f" I have chosen a number between {low} and {high}. Try to guess it! ")

        while True:
            try:
                guess = int(input(" Enter your guess : "))
                attempts += 1
            except ValueError:
                print(" Invalid input! Enter a number. ")
                continue

            if guess < secret_number:
                print(" Too low! Try again. ")
            elif guess > secret_number:
                print(" Too high! Try again. ")
            else:
                print(f" Correct! You guessed it in {attempts} attempts. ")
                break

        if best_attempt is None or attempts < best_attempt:
            best_attempt = attempts

        print(f" Best score so far : {best_attempt} attempts ")

        play_again = input(" Do you want to play again ? (y/n) : ").lower()
        if play_again != 'y':
            print(" Thanks for playing! ")
            break


guessing_game()