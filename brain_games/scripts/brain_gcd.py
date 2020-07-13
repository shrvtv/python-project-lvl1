#!/usr/bin/env python3
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
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)
    print('')

    while brain_games.cli.start < brain_games.cli.end:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        brain_games.cli.right_answer_int = get_gcd(first_number, second_number)
        print(brain_games.cli.question + str(first_number) + ' ' + str(second_number))
        answer = int(prompt.string('Your answer: '))
        if answer == brain_games.cli.right_answer_int:
            print('Correct!')
            brain_games.cli.start += 1
        else:
            brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_int)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
