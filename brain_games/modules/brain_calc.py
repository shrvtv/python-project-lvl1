import random
import operator
import brain_games.cli


def get_list():
    operations = ['+', '-', '*']
    right_answer = ''
    result = []
    tries = 3
    result.append('What is the result of the expression?')

    while tries:
        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        operation = random.choice(operations)

        if operation == '+':
            right_answer = str(operator.add(first_number, second_number))

        elif operation == '-':
            right_answer = str(operator.sub(first_number, second_number))

        elif operation == '*':
            right_answer = str(operator.mul(first_number, second_number))

        string = '{} {} {}'.format(str(first_number), operation, str(second_number))
        result.append((string, right_answer))
        tries -= 1
    return result


def main():
    brain_games.cli.engine(get_list())
