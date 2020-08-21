import random
import brain_games.cli


dictionary = {True: 'yes', False: 'no'}
description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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


def get_question_and_answer():
    result = []
    tries = 3
    number = random.randint(1, 100)

    right_answer = str(dictionary.get(is_prime(number)))

    question = str(number)
    return question, right_answer


def start_game():
    brain_games.cli.engine(get_question_and_answer, description)
