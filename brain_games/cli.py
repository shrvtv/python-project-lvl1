import prompt


def check_answer(answer, right_answer):
    if answer == right_answer:
        return True
    else:
        return False


def engine(function, description):
    amount_of_tries = 3
    print('Welcome to the Brain Games!')
    print(description, end='\n\n')
    name = prompt.string('May I have your name? ')
    print('{}, {}!'.format('Hello', name), end='\n\n')

    while amount_of_tries:
        question, right_answer = function()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')

        if check_answer(answer, right_answer):
            print('Correct!')
            amount_of_tries -= 1
        else:
            print(str(answer) + ' is wrong answer ;(. Correct answer was ' + str(right_answer))
            print("Let's try again, " + name + '!')
    print('{}, {}!'.format('Congratulations', name))
