import prompt
import random
import brain_games.cli


def main():
    tries = 3
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while tries:

        number = random.randint(0, 1000)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        print('Question: ' + str(number))

        answer = prompt.string('Your answer: ')

        if brain_games.cli.check_answer(answer, right_answer):
            print('Correct!')
            tries -= 1
        else:
            brain_games.cli.wrong_answer(answer, right_answer)
            brain_games.cli.try_again(name)

    brain_games.cli.congrats(name)
