import prompt
import random
import brain_games.cli

right_answer = 0


def line():
    global right_answer

    step = random.randint(1, 10)
    number = random.randint(0, 100)
    start_line = 0
    end_line = 10
    secret_number = random.randint(start_line, end_line - 1)

    print('Question: ', end='')

    while start_line < end_line:
        if start_line == secret_number:
            right_answer = number
            print('..', end=' ')
            number += step
        else:
            print(number, end=' ')
            number += step
        start_line += 1
    print('')


def main():

    brain_games.cli.start()

    while brain_games.cli.tries:
        line()
        answer = prompt.integer('Your answer: ')
        brain_games.cli.check_answer(answer, right_answer)

    brain_games.cli.congrats()
