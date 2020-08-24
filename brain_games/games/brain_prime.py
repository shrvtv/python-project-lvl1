import random
import brain_games.cli


DICTIONARY = {True: 'yes', False: 'no'}
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False

    i = 2
    while i < number / 2:
        if number % i == 0:
            return False
        else:
            i += 1
    return True


def get_question_and_answer():
    number = random.randint(1, 100)

    right_answer = str(DICTIONARY.get(is_prime(number)))

    question = str(number)
    return question, right_answer


def start_game():
    brain_games.cli.start_game(get_question_and_answer, DESCRIPTION)
