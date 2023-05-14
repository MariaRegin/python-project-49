import prompt


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    wins = 0
    while wins < 3:
        question, right_answer = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
            wins += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')
