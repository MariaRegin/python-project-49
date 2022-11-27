#!/usr/bin/env python3
import random


TASK = 'What is the result of the expression?'


def operation_result():
    random_number1 = random.randint(0,1000)
    random_number2 = random.randint(0,1000)
    random_number1 = str(random_number1)
    random_number2 = str(random_number2)
    expression1 = random_number1 + ' * ' + random_number2
    expression2 = random_number1 + ' - ' + random_number2
    expression3 = random_number1 + ' + ' + random_number2
    expressions_list = [expression1, expression2, expression3]
    number = random.choice(expressions_list)
    splitted_expression = number.split()
    first_number = int(splitted_expression[0])
    second_number = int(splitted_expression[2])
    sign = splitted_expression[1]
    if sign == '*':
        result = first_number * second_number
    if sign == '+':
        result = first_number + second_number
    if sign == '-':
        result = first_number - second_number
    right_answer = str(result)
    return number, right_answer
