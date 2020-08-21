import random
import brain_games.cli


def get_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    c = a + b
    return c


description = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = random.randint(1, 25)
    second_number = random.randint(1, 25)

    right_answer = str(get_gcd(first_number, second_number))
    string = '{} {}'.format(str(first_number), str(second_number))
    return string, right_answer


def start_game():
    brain_games.cli.engine(get_question_and_answer, description)
