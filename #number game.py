#number game
import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    # Pick a secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Guess a number between 1 and 100: ")
        
        # Make sure the user entered a valid number
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
            
        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
