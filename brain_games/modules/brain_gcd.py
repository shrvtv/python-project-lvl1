import random


def get_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    c = a + b
    return c


def main():
    result = []
    list = 3

    while list:

        first_number = random.randint(1, 25)
        second_number = random.randint(1, 25)

        right_answer = str(get_gcd(first_number, second_number))

        question = '{}: {} {}'.format('Question', str(first_number), str(second_number))

        result.append((question, right_answer))

        list -= 1
    return result
