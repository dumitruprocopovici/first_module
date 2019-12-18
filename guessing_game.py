import random


def read_number(min_val, max_val):
    return int(
        input("Enter an integer from {} to {}: ".format(min_val, max_val)))


def guessing_the_number(min_val, max_val):
    guess = read_number(min_val, max_val)
    random_number = random.randint(min_val, max_val)
    while random_number != guess:
        if guess < random_number:
            print("guess is low")
            guess = read_number(min_val, max_val)
        elif guess > random_number:
            print("guess is high")
            guess = read_number(min_val, max_val)
        else:
            break
    print("you guessed it!")


def main():
    for i in range(10):
        guessing_the_number(1, 99)

    for i in range(10):
        guessing_the_number(1, 49)


if __name__ == "__main__":
    main()
