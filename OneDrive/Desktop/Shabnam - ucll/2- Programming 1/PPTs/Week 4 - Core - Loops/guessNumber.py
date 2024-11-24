def guess_number(number):
    guess = None
    while guess != number:
        guess = int(input("Guess number:"))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Correct!")


# alternative
def guess_number(number):
    guess = None
    while guess != number:
        guess = int(input("Guess number:"))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Correct!")


guess_number(317)