#!/usr/bin/env python3
import random
import brain_games.cli


def main():
    brain_games.cli.welcome()
    print('Find the greatest common divisor of given numbers.')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)
    print('')
    
    while brain_games.cli.start < brain_games.cli.end:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        brain_games.cli.right_answer_int = brain_games.cli.get_gcd(first_number, second_number)
        print(brain_games.cli.question + str(first_number) + ' ' + str(second_number))
        answer = int(brain_games.cli.get_answer())
        if answer == brain_games.cli.right_answer_int:
            brain_games.cli.correct()
            brain_games.cli.start += 1
        else:
            brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_int)
    brain_games.cli.congrats(name)


if __name__ == '__main__':
    main()
