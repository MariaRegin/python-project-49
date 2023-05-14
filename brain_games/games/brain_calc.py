#!/usr/bin/env python3
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    random_number1 = random.randint(0, 1000)
    random_number2 = random.randint(0, 1000)
    signs_list = ["*", "-", "+"]
    random_sign = random.choice(signs_list)
    question = str(random_number1) + random_sign + str(random_number2)
    right_answer = define_sign(random_number1, random_number2, random_sign)
    return question, str(right_answer)


def define_sign(number1, number2, sign):
    if sign == '*':
        expression_result = number1 * number2
    if sign == '+':
        expression_result = number1 + number2
    if sign == '-':
        expression_result = number1 - number2
    return expression_result
