#!/usr/bin/env python3
import random
import brain_games.cli


def main():
    brain_games.cli.welcome()
    print('What number is missing in the progression?')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)
    print('')
    
    while brain_games.cli.start < brain_games.cli.end:
        step = random.randint(1, 10)
        first_number = random.randint(0, 100)
        start = 0
        end = 10
        secret_number = random.randint(0, 9)
        print(brain_games.cli.question, end='')
        while start < end:
            if start == secret_number:
                brain_games.cli.right_answer_int = first_number
                print('..', end = ' ')
                first_number += step
            else:
                print(first_number, end=' ')
                first_number += step
            start += 1
        print('')
        answer = int(brain_games.cli.get_answer())
        if answer == brain_games.cli.right_answer_int:
            brain_games.cli.correct()
            brain_games.cli.start += 1
        else:
            brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_int)
    brain_games.cli.congrats(name)
if __name__ == '__main__':
    main()