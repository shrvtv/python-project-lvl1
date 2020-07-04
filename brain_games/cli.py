import prompt

question = 'Question: '
answer = 'Answer '
counter = 0
right_answer = ''
correct = 'Correct!'


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def wrong_answer(answer):
    print(answer + ' is wrong answer ;(. Correct answer was ' + right_answer)


def welcome():
        print('Welcome to the Brain Games!')


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def hello(user):
    print('{}, {}!'.format('Hello', user))


def congratulations(user):
        print('{}, {}!'.format('Congratulations', user))


def try_again(user):
        print("Let's try again, " + user + '!')
