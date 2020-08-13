import random
import brain_games.cli


def get_list():
    result = []
    tries = 3
    string = 'What number is missing in the progression?'
    result.append(string)

    while tries:
        right_answer = ''
        pointer = 0
        string = ''
        step = random.randint(1, 10)
        number = random.randint(0, 100)
        secret_number_position = random.randint(0, 10)

        while pointer < 10:
            if pointer == secret_number_position:
                right_answer = str(number)
                string += ' .. '
                number += step
            else:
                string += str(number) + ' '
                number += step
            pointer += 1

        result.append((string, right_answer))
        tries -= 1
    return result


def main():
    brain_games.cli.engine(get_list())
