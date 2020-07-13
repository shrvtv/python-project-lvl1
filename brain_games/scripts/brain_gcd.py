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
    start = 0
    end = 3
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while start < end:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        right_answer = get_gcd(first_number, second_number)
        print('{}: {} {}'.format('Question', str(first_number), str(second_number)))
        answer = prompt.integer('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            start += 1
        else:
            brain_games.cli.wrong_answer(answer, right_answer)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
