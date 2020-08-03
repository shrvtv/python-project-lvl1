import prompt
import random
import operator
import brain_games.cli


def main():
    brain_games.cli.start()
    operations = ['addition', 'subtraction', 'multiplication']

    while brain_games.cli.tries:

        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        operation = random.choice(operations)

        if operation == 'addition':
            right_answer = operator.add(first_number, second_number)
            print('{}: {} + {}'.format('Question', str(first_number), str(second_number)))
            answer = prompt.integer('Your answer: ')
            brain_games.cli.check_answer(answer, right_answer)

        elif operation == 'subtraction':
            right_answer = operator.sub(first_number, second_number)
            print('{}: {} - {}'.format('Question', str(first_number), str(second_number)))
            answer = prompt.integer('Your answer: ')
            brain_games.cli.check_answer(answer, right_answer)

        elif operation == 'multiplication':
            right_answer = operator.mul(first_number, second_number)
            print('{}: {} * {}'.format('Question', str(first_number), str(second_number)))
            answer = prompt.integer('Your answer: ')
            brain_games.cli.check_answer(answer, right_answer)

    brain_games.cli.congrats()
