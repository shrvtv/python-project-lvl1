#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print('{}, {}!'.format('Hello', name))

    i = 0
    while i < 3:
        number = random.randint(0, 1000)
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(answer + ' is wrong answer ;(. Correct answer was ' + right_answer)
            print("Let's try again, " + name)
    print('{}, {}!'.format('Congratulations', name))


if __name__ == '__main__':
    main()
