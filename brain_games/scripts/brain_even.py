#!/usr/bin/env python3
import random
import brain_games.cli


def main():
    brain_games.cli.welcome()
    print('Answer "yes" if number even otherwise answer "no".')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while brain_games.cli.counter < 3:
        number = random.randint(0, 1000)
        if number % 2 == 0:
            brain_games.cli.right_answer = 'yes'
        else:
            brain_games.cli.right_answer = 'no'
        print(brain_games.cli.question + str(number))
        answer = brain_games.cli.get_answer()
        if answer == brain_games.cli.right_answer:
            print(brain_games.cli.correct)
            brain_games.cli.counter += 1
        else:
            brain_games.cli.wrong_answer(answer)
            brain_games.cli.try_again(name)
    brain_games.cli.congratulations(name)


if __name__ == '__main__':
    main()
