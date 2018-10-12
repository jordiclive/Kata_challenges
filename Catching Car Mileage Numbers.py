"""Kata can be found at https://www.codewars.com/kata/calculator/train/python"""

# Coding Eval calculator from scratch

Division = lambda x, i: str(float(x[i-1]) / float(x[i+1]))

Multiplication = lambda x, i: str(float(x[i-1]) * float(x[i+1]))

Subtraction = lambda x, i: str(float(x[i-1]) - float(x[i+1]))

Addition = lambda x, i: str(float(x[i-1]) + float(x[i+1]))

ops = {'/' : Division, '*' : Multiplication, '-' : Subtraction, '+' : Addition}


def BODMAS(calc_str, operand='/'):
    while '' in calc_str:
        calc_str.remove('')
    if '/' not in calc_str:
        operand = '*'
        if '*' not in calc_str:
            operand = '-'
            if '-' not in calc_str:
                operand = '+'
                if '+' not in calc_str:
                    return float(calc_str[0])
    for i in range(len(calc_str)-1):
        if calc_str[i] == operand:
            calc_str[i] = ops[operand](calc_str, i)
            calc_str[i - 1], calc_str[i + 1] = '', ''
            return BODMAS(calc_str)


class Calculator(object):

    def evaluate(self,initial_str):
        initial_list = [k for k in initial_str.split()]
        return BODMAS(initial_list)





