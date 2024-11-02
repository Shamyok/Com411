import random

def play_guess_the_number():
    min_value = int(input("Please enter the minimum value: "))
    max_value = int(input("Please enter the maximum value: "))

    ran_num = random.randint(min_value, max_value)
    user_guess = int(input(f"I am thinking of a number between {min_value} and {max_value}. Can you guess what it is?"))

    while user_guess != ran_num:
        if user_guess > ran_num:
            print("Your guess is too high.")
            user_guess = int(input("Try again"))

        elif user_guess < ran_num:
            print("Your guess is too low.")
            user_guess = int(input("Try again"))

    if user_guess == ran_num:
            print("Congrats! You guessed my number!")

play_guess_the_number()