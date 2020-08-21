import random
import brain_games.cli


description = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(0, 1000)

    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    question = str(number)
    return question, right_answer


def start_game():
    brain_games.cli.engine(get_question_and_answer, description)
