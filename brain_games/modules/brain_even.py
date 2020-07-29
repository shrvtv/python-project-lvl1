import prompt
import random
import brain_games.cli


def main():

    brain_games.cli.start()

    while brain_games.cli.tries:

        number = random.randint(0, 1000)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        print('Question: ' + str(number))

        answer = prompt.string('Your answer: ')

        brain_games.cli.check_answer(answer, right_answer)

    brain_games.cli.congrats()
