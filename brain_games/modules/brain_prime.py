import prompt
import random
import brain_games.cli


def is_prime(number):
    i = 1
    while i <= number:
        if number % i == 0 and i != 1 and i != number:
            return 'no'
        else:
            i += 1
    return 'yes'


def main():

    brain_games.cli.start()

    while brain_games.cli.tries:

        number = random.randint(1, 100)

        right_answer = is_prime(number)

        print('Question: ' + str(number))

        answer = prompt.string('Your answer: ')
        brain_games.cli.check_answer(answer, right_answer)

    brain_games.cli.congrats()
