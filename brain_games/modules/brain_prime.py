import random
import brain_games.cli


dictionary = {True: 'yes', False: 'no'}


def is_prime(number):
    if number <= 1:
        return False
    i = 1
    while i <= number / 2:
        if number % i == 0 and i != 1 and i != number:
            return False
        else:
            i += 1
    return True


def get_list():
    result = []
    tries = 3
    result.append('Answer "yes" if given number is prime. Otherwise answer "no".')

    while tries:

        number = random.randint(1, 100)

        right_answer = str(dictionary.get(is_prime(number)))

        string = str(number)

        result.append((string, right_answer))

        tries -= 1
    return result


def start_game():
    brain_games.cli.engine(get_list())
