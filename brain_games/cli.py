import prompt

question = 'Question: '
start = 0
end = 3
right_answer_string = ''
right_answer_int = 0


def wrong_answer(answer, right_answer):
    print(str(answer) + ' is wrong answer ;(. Correct answer was ' + str(right_answer))


def get_name():
    print('')
    name = prompt.string('May I have your name? ')
    return name


def hello(user):
    print('{}, {}!'.format('Hello', user))


def congrats(user):
        print('{}, {}!'.format('Congratulations', user))


def try_again(user):
        print("Let's try again, " + user + '!')
