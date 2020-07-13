#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def main():
    start = 0
    end = 3
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while start < end:

        number = random.randint(0, 1000)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        print('Question: ' + str(number))

        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
            start += 1
        else:
            brain_games.cli.wrong_answer(answer, right_answer)
            brain_games.cli.try_again(name)

    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
