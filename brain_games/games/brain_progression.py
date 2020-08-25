import random
import brain_games.cli


DESCRIPTION = 'What number is missing in the progression?'


def get_progression(number, step, length):
    result = []
    while length:
        result.append(number)
        number += step
        length -= 1
    return result


def get_question_and_answer():
    LENGTH = 10
    step = random.randint(1, 10)
    number = random.randint(0, 100)
    progression = get_progression(number, step, LENGTH)
    secret_number_position = random.randint(0, LENGTH)
    secret_number = str(progression[secret_number_position])
    progression[secret_number_position] = '..'

    progression = map(str, progression)
    question = ' '.join(progression)
    return question, secret_number


def start_game():
    brain_games.cli.play(get_question_and_answer, DESCRIPTION)
