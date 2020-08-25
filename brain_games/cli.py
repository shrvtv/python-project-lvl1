import prompt


def check_answer(answer, right_answer):
    return answer == right_answer


def play(get_question_and_answer, description):
    AMOUNT_OF_TRIES = 3
    print('Welcome to the Brain Games!')
    print(description, end='\n\n')
    name = prompt.string('May I have your name? ')
    print('{}, {}!'.format('Hello', name), end='\n\n')

    while AMOUNT_OF_TRIES:
        question, right_answer = get_question_and_answer()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')

        if check_answer(answer, right_answer):
            print('Correct!')
            AMOUNT_OF_TRIES -= 1
        else:
            print(str(answer) + ' is wrong answer ;(. Correct answer was ' + str(right_answer))
            print("Let's try again, " + name + '!')
    print('{}, {}!'.format('Congratulations', name))
