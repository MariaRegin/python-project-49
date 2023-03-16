#!/usr/bin/env python3
import random


DESCRIPTION = 'What is the result of the expression?'


def get_result():
    random_number1 = random.randint(0, 1000)
    random_number2 = random.randint(0, 1000)
    expression1 = f"{random_number1} * {random_number2}"
    expression2 = f"{random_number1} - {random_number2}"
    expression3 = f"{random_number1} + {random_number2}"
    expressions_list = [expression1, expression2, expression3]
    task = random.choice(expressions_list)
    splitted_list = task.split()
    first_number = int(splitted_list[0])
    sign = splitted_list[1]
    second_number = int(splitted_list[2])
    def define_sign():
        if sign == '*':
            result = first_number * second_number
        if sign == '+':
            result = first_number + second_number
        if sign == '-':
            result = first_number - second_number
        preliminary_answer = str(result)
        return preliminary_answer
    right_answer = define_sign()
    return task, right_answer
