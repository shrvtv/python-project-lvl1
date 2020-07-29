import prompt
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


def main():

    brain_games.cli.start()

    while brain_games.cli.tries:

        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)

        right_answer = get_gcd(first_number, second_number)

        print('{}: {} {}'.format('Question', str(first_number), str(second_number)))

        answer = prompt.integer('Your answer: ')

        brain_games.cli.check_answer(answer, right_answer)

    brain_games.cli.congrats()
