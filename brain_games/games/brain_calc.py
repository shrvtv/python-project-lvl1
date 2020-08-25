import random
import operator
import brain_games.cli


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operations = ['+', '-', '*']
    right_answer = 0

    first_number = random.randint(1, 25)
    second_number = random.randint(1, 25)
    operation = random.choice(operations)

    if operation == '+':
        right_answer = operator.add(first_number, second_number)

    elif operation == '-':
        right_answer = operator.sub(first_number, second_number)

    elif operation == '*':
        right_answer = operator.mul(first_number, second_number)

    question = '{} {} {}'.format(str(first_number), operation, str(second_number))
    return question, str(right_answer)


def start_game():
    brain_games.cli.play(get_question_and_answer, DESCRIPTION)
