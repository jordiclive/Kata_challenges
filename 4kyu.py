"""Multiple 4kyu Kata"""


#https://www.codewars.com/kata/5672682212c8ecf83e000050, grade: 4kyu


def dbl_linear(n):
    u = [1]
    x, y = 0, 0
    for i in range(n):
        nextX = 2*u[x] + 1
        nextY = 3*u[y] + 1
        if nextX <= nextY:
            u.append(nextX)
            x += 1
            if nextX == nextY:
                y += 1
        else:
            u.append(nextY)
            y += 1
    return u[n]


#https://www.codewars.com/kata/range-extraction/train/python, grade: 4kyu


def solution(args):
    if type(args) == list:
        num_list = args[:]
        num_list.append(0)
        index, new_str, n = 0, '', 3
        while index < len(num_list):
            if index < len(num_list)-2:
                if num_list[index] == num_list[index+1] - 1 == num_list[index+2] - 2:
                    while num_list[index] == num_list[index+n]-n:
                        n += 1
                    new_str += ',' + str(num_list[index]) + '-' + str(num_list[index+n-1])
                    index += n
                    n = 3
                else:
                    new_str += ',' + str(num_list[index])
                    index += 1
            else:
                new_str += ',' + str(num_list[index])
                index += 1
        new_str = new_str[:-2]
        return new_str[1:]
    if type(args) == str:
        return args

"""Kata can be found at https://www.codewars.com/kata/catching-car-mileage-numbers/train/python, grade: 4kyu"""
import numpy as np


def doubles(maxk, maxn):
    Base = np.ones((maxk, maxn))
    for k in range(maxk):
        for n in range(maxn):
            Base[k, n] = 1/((k+1)*(n+2)**(2*(k+1)))
    return Base.sum()







