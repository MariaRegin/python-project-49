import prompt


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.DESCRIPTION)
    tries = 0
    while tries < 3:
        tries += 1
        task, right_answer = game.calculate_result()
        print(f"Question: {task}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')
