#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def main():
    start = 0
    end = 3
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while start < end:
        step = random.randint(1, 10)
        number = random.randint(0, 100)
        start_line = 0
        end_line = 10
        secret_number = random.randint(0, 9)
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
        answer = prompt.integer('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            start += 1
        else:
            brain_games.cli.wrong_answer(answer, right_answer)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
