"""This module runs a number guessing game with multiple levels."""

import random

def welcome():
    """Prints a welcome message and the game rules."""
    print("Welcome to the Number Guessing Game!")
    print("You have 3 levels to beat.")
    print("Level 1: 1-10, Level 2: 1-50, Level 3: 1-100")
    print("You get 5 tries in each level.\n")


def play_level(level, max_num):
    """Plays one level of the game.
    
    Args:
        level (int): The current level number.
        max_num (int): The upper bound for the number to guess.

    Returns:
        tuple: A boolean for success and the score earned.
    """
    secret = random.randint(1, max_num)
    attempts = 5
    score = 0
    print(f"\nLevel {level}: Guess a number between 1 and {max_num}")

    for i in range(attempts):
        try:
            guess = int(input(f"Attempt {i+1}: "))
        except ValueError:
            print("Invalid input. Try a number.")
            continue

        if guess == secret:
            print("Correct! You move to the next level.")
            score += (max_num - i * 5)
            return True, score
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Sorry, the correct number was {secret}. Game Over.")
    return False, score


def main():
    """Main function to run the full game."""
    welcome()
    total_score = 0
    levels = [(1, 10), (2, 50), (3, 100)]

    for level, max_num in levels:
        success, score = play_level(level, max_num)
        total_score += score
        if not success:
            break

    print(f"\nYour final score: {total_score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
