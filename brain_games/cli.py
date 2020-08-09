import prompt


def check_answer(answer, right_answer):
    if answer == right_answer:
        print('Correct!')
        return True
    else:
        line = ' is wrong answer ;(. Correct answer was '
        print(str(answer) + line + str(right_answer))
        return False


def engine(questions_and_answers):
    tries = 1
    print('Welcome to the Brain Games!')
    print(questions_and_answers[0], end='\n\n')
    name = prompt.string('May I have your name? ')
    print('{}, {}!'.format('Hello', name), end='\n\n')
    question = 'Question: '

    while tries <= 3:
        string, right_answer = questions_and_answers[tries]
        print(question + string)
        answer = prompt.string('Your answer: ')

        if check_answer(answer, right_answer):
            tries += 1
        else:
            print("Let's try again, " + name + '!')

    print('{}, {}!'.format('Congratulations', name))
