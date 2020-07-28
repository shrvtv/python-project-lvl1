import prompt
import random
import brain_games.cli


def main():
    tries = 3
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    operations = ['addition', 'subtraction', 'multiplication']
    name = brain_games.cli.get_name()
    brain_games.cli.hello(name)

    while tries:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        operation = random.choice(operations)

        if operation == 'addition':
            right_answer = first_number + second_number
            print('{}: {} + {}'.format('Question', str(first_number), str(second_number)))
            answer = prompt.integer('Your answer: ')
            if brain_games.cli.check_answer(answer, right_answer):
                print('Correct!')
                tries -= 1
            else:
                brain_games.cli.wrong_answer(answer, right_answer)
                brain_games.cli.try_again(name)

        elif operation == 'subtraction':
            right_answer = first_number - second_number
            print('{}: {} - {}'.format('Question', str(first_number), str(second_number)))
            answer = prompt.integer('Your answer: ')
            if brain_games.cli.check_answer(answer, right_answer):
                print('Correct!')
                tries -= 1
            else:
                brain_games.cli.wrong_answer(answer, right_answer)
                brain_games.cli.try_again(name)

        elif operation == 'multiplication':
            right_answer = first_number * second_number
            print('{}: {} * {}'.format('Question', str(first_number), str(second_number)))
            answer = prompt.integer('Your answer: ')
            if brain_games.cli.check_answer(answer, right_answer):
                print('Correct!')
                tries -= 1
            else:
                brain_games.cli.wrong_answer(answer, right_answer)
                brain_games.cli.try_again(name)

    brain_games.cli.congrats(name)
