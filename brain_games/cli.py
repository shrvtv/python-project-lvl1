import prompt


def check_answer(answer, right_answer):
    if answer == right_answer:
        print('Correct!')
        return True
    else:
        line = ' is wrong answer ;(. Correct answer was '
        print(str(answer) + line + str(right_answer))
        return False


def engine(list):
    tries = 2
    name = ''
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?', end='\n\n')
    name = prompt.string('May I have your name? ')
    print('{}, {}!'.format('Hello', name), end='\n\n')
    while tries > -1:
        question, right_answer = list[tries]
        print(question)
        answer = prompt.string('Your answer: ')
        if check_answer(answer, right_answer):
            tries -= 1
        else:
            print("Let's try again, " + name + '!')

    print('{}, {}!'.format('Congratulations', name))
