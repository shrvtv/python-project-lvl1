import random
import brain_games.cli


description = 'What number is missing in the progression?'


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


def get_question_and_answer():
    progression = get_progression()
    secret_number_position = random.randint(0, 10)

    secret_number = str(progression[secret_number_position])
    progression[secret_number_position] = '..'

    progression = map(str, progression)
    question = ' '.join(progression)
    return question, secret_number


def start_game():
    brain_games.cli.engine(get_question_and_answer, description)
