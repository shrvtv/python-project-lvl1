#!/usr/bin/env python3
import random
import brain_games.cli


def main():
    brain_games.cli.welcome()
    print('What is the result of the expression?')
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while brain_games.cli.start < brain_games.cli.end:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        operation = random.randint(1, 3)
        
        if operation == 1:
            #* addition
            brain_games.cli.right_answer_int = first_number + second_number
            print(brain_games.cli.question + str(first_number) + ' + ' + str (second_number))
            answer = int(brain_games.cli.get_answer())
            if answer == brain_games.cli.right_answer_int:
                brain_games.cli.correct()
                brain_games.cli.start += 1
            else:
                brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_int)
        
        if operation == 2:
            #* subtraction
            brain_games.cli.right_answer_int = first_number - second_number
            print(brain_games.cli.question + str(first_number) + ' - ' + str (second_number))
            answer = int(brain_games.cli.get_answer())
            if answer == brain_games.cli.right_answer_int:
                brain_games.cli.correct()
                brain_games.cli.start += 1
            else:
                brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_int)
        
        if operation == 3:
            #* multiplication
            brain_games.cli.right_answer_int = first_number * second_number
            print(brain_games.cli.question + str(first_number) + ' * ' + str (second_number))
            answer = int(brain_games.cli.get_answer())
            if answer == brain_games.cli.right_answer_int:
                brain_games.cli.correct()
                brain_games.cli.start += 1
            else:
                brain_games.cli.wrong_answer(answer, brain_games.cli.right_answer_int)
    brain_games.cli.congrats(name)

if __name__ == '__main__':
    main()