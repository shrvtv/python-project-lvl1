#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def main():
    start = 0
    end = 3
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while start < end:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        operation = random.randint(1, 3)

        if operation == 1:
            # * addition
            right_answer = first_number + second_number
            print('Question: ' + str(first_number) + ' + ' + str(second_number))
            answer = prompt.integer('Your answer: ')
            start = brain_games.cli.check_answer(start, name, answer, right_answer)

        if operation == 2:
            # * subtraction
            right_answer = first_number - second_number
            print('Question: ' + str(first_number) + ' - ' + str(second_number))
            answer = prompt.integer('Your answer: ')
            start = brain_games.cli.check_answer(start, name, answer, right_answer)

        if operation == 3:
            # * multiplication
            right_answer = first_number * second_number
            print('Question: ' + str(first_number) + ' * ' + str(second_number))
            answer = prompt.integer('Your answer: ')
            start = brain_games.cli.check_answer(start, name, answer, right_answer)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
