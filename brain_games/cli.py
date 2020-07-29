import prompt


tries = 3
name = ''


def congrats():
    global name
    print('{}, {}!'.format('Congratulations', name))


def start():
    global name
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?', end='\n\n')
    name = prompt.string('May I have your name? ')
    print('{}, {}!'.format('Hello', name), end='\n\n')


def check_answer(answer, right_answer):
    global tries, name
    if answer == right_answer:
        print('Correct!')
        tries -= 1
    else:
        line = ' is wrong answer ;(. Correct answer was '
        print(str(answer) + line + str(right_answer))
        print("Let's try again, " + name + '!')
