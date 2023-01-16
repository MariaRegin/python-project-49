#!/usr/bin/env python3

import prompt


def launch_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game_module.TASK)
    tries = 0
    while tries < 3:
        tries += 1
        number, right_answer = game_module.operation_result()
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            break
    else:
        print('Congratulations, ' + name + '!')
