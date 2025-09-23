import random

def test_random():
    random_number = random.randint(1, 10)
    print("==Guess Number between(1-10)==")
    guess_number= input("what is your guess number:")
    guess_number= input(guess_number)

    if random_number == guess_number:
        print("Congrations!")

    elif random_number < guess_number:
        print("Too high")

    elif random_number > guess_number:
        print("Too low")

        #rint(random_number)
test_random()