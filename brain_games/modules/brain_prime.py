import random


dictionary = {True: 'yes', False: 'no'}


def is_prime(number):
    i = 1
    while i <= number:
        if number % i == 0 and i != 1 and i != number:
            return False
        else:
            i += 1
    return True


def main():
    result = []
    list = 3

    while list:

        number = random.randint(1, 100)

        right_answer = str(dictionary.get(is_prime(number)))

        question = ('Question: ' + str(number))

        result.append((question, right_answer))

        list -= 1
    return result
