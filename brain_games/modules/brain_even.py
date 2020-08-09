import random
import brain_games.cli


def get_list():
    result = []
    tries = 3
    string = 'Answer "yes" if number even otherwise answer "no".'
    result.append(string)

    while tries:

        number = random.randint(0, 1000)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        question = ('Question: ' + str(number))
        result.append((question, right_answer))

        tries -= 1
    return result


def main():
    brain_games.cli.engine(get_list())
