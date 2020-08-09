import random
import brain_games.cli


def get_list():
    result = []
    tries = 3
    string = 'What number is missing in the progression?'
    result.append(string)

    while tries:
        right_answer = 0
        step = random.randint(1, 10)
        number = random.randint(0, 100)
        start_line = 0
        end_line = 10
        secret_number = random.randint(start_line, end_line - 1)
        string = ''

        while start_line < end_line:
            if start_line == secret_number:
                right_answer = str(number)
                string += ' .. '
                number += step
            else:
                string += str(number) + ' '
                number += step
            start_line += 1

        result.append((string, right_answer))
        tries -= 1
    return result


def main():
    brain_games.cli.engine(get_list())
