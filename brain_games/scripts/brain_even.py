#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)
    print('')

    while brain_games.cli.start < brain_games.cli.end:

        number = random.randint(0, 1000)

        if number % 2 == 0:
            brain_games.cli.right_answer_string = 'yes'
        else:
            brain_games.cli.right_answer_string = 'no'

        print(brain_games.cli.question + str(number))

        answer = prompt.string('Your answer: ')

        if answer == brain_games.cli.right_answer_string:
            print('Correct!')
            brain_games.cli.start += 1
        else:
            brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_string)
            brain_games.cli.try_again(name)

    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
