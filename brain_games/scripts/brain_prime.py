#!/usr/bin/env python3
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
    start = 0
    end = 3
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while start < end:
        number = random.randint(1, 100)
        right_answer = is_prime(number)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        start = brain_games.cli.check_answer(start, name, answer, right_answer)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
