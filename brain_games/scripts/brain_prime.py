#!/usr/bin/env python3
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
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)
    print('')
    while brain_games.cli.start < brain_games.cli.end:
        number = random.randint(1, 100)
        brain_games.cli.right_answer_string = is_prime(number)
        print(brain_games.cli.question + str(number))
        answer = brain_games.cli.get_answer()
        if answer == brain_games.cli.right_answer_string:
            print('Correct!')
            brain_games.cli.start += 1
        else:
            brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_string)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
