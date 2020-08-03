import random
import operator


def main():
    operations = ['addition', 'subtraction', 'multiplication']
    result = []
    question = ''
    right_answer = 0
    list = 3

    while list:

        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)
        operation = random.choice(operations)

        if operation == 'addition':
            right_answer = str(operator.add(first_number, second_number))
            question = '{}: {} + {}'.format('Question', str(first_number), str(second_number))
            result.append((question, right_answer))
            list -= 1

        elif operation == 'subtraction':
            right_answer = str(operator.sub(first_number, second_number))
            question = '{}: {} - {}'.format('Question', str(first_number), str(second_number))
            result.append((question, right_answer))
            list -= 1

        elif operation == 'multiplication':
            right_answer = str(operator.mul(first_number, second_number))
            question = '{}: {} * {}'.format('Question', str(first_number), str(second_number))
            result.append((question, right_answer))
            list -= 1
    return result
