import random


def play_game():
    try:
        lower_range = int(input('Enter the lower range: '))
        upper_range = int(input('Enter the upper range: '))
        if upper_range <= lower_range:
            print(
                "Please enter valid integer values where upper range is greater than lower range")
            return
    except ValueError:
        print("Please enter integer values")
        return

    random_number = random.randint(lower_range, upper_range)
    print(random_number)  # Debug line, can be removed

    while True:
        try:
            guess_number = int(input('Enter the guess number: '))
        except ValueError:
            print("Please enter integer values")
            continue

        if random_number == guess_number:
            print('Congratulations! You guessed it correctly.')
            break
        else:
            if guess_number < random_number:
                lower_range = guess_number + 1
            else:
                upper_range = guess_number - 1
            print(f'Guess a number between {lower_range} and {upper_range}')


if __name__ == "__main__":
    play_game()
