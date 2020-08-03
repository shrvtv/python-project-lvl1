import random


def main():
    result = []
    list = 3

    while list:

        number = random.randint(0, 1000)

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        question = ('Question: ' + str(number))

        result.append((question, right_answer))

        list -= 1
    return result
