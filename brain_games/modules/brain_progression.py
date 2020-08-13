import random
import brain_games.cli


def get_progression():
    i = 0
    result = []
    step = random.randint(1, 10)
    number = random.randint(0, 100)

    while i < 10:
        result.append(number)
        number += step
        i += 1
    return result


def get_string_and_answer():
    progression = get_progression()
    secret_number_position = random.randint(0, 10)

    secret_number = str(progression[secret_number_position])
    progression[secret_number_position] = '..'

    progression = map(str, progression)
    string = ' '.join(progression)
    return string, secret_number


def get_list():
    result = []
    tries = 3
    result.append('What number is missing in the progression?')

    while tries:
        result.append(get_string_and_answer())
        tries -= 1
    return result


def main():
    brain_games.cli.engine(get_list())
