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


def get_list():
    result = []
    tries = 3
    result.append('Find the greatest common divisor of given numbers.')

    while tries:

        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)

        right_answer = str(get_gcd(first_number, second_number))
        string = '{} {}'.format(str(first_number), str(second_number))
        result.append((string, right_answer))

        tries -= 1
    return result


def main():
    brain_games.cli.engine(get_list())
