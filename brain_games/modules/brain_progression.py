import random


def main():
    result = []
    list = 3

    while list:
        right_answer = 0
        step = random.randint(1, 10)
        number = random.randint(0, 100)
        start_line = 0
        end_line = 10
        secret_number = random.randint(start_line, end_line - 1)

        question = 'Question: '

        while start_line < end_line:
            if start_line == secret_number:
                right_answer = str(number)
                question += ' .. '
                number += step
            else:
                question += str(number) + ' '
                number += step

            start_line += 1

        result.append((question, right_answer))

        list -= 1
    return result
