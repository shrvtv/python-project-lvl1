#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def addition(name, first_number, second_number):
    right_answer = first_number + second_number
    print('{}: {} + {}'.format('Question', str(first_number), str(second_number)))
    answer = prompt.integer('Your answer: ')
    if brain_games.cli.check_answer(name, answer, right_answer):
        return True


def subtraction(name, first_number, second_number):
    right_answer = first_number - second_number
    print('{}: {} - {}'.format('Question', str(first_number), str(second_number)))
    answer = prompt.integer('Your answer: ')
    if brain_games.cli.check_answer(name, answer, right_answer):
        return True


def multiplication(name, first_number, second_number):
    right_answer = first_number * second_number
    print('{}: {} * {}'.format('Question', str(first_number), str(second_number)))
    answer = prompt.integer('Your answer: ')
    if brain_games.cli.check_answer(name, answer, right_answer):
        return True


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
            if addition(name, first_number, second_number):
                start += 1

        elif operation == 2:
            # * subtraction
            if subtraction(name, first_number, second_number):
                start += 1

        elif operation == 3:
            # * multiplication
            if multiplication(name, first_number, second_number):
                start += 1

    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
