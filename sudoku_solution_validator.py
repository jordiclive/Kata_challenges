'''https://www.codewars.com/kata/sudoku-solution-validator/train/python, 4kyu'''


# Essentially function to assert whether the input is a valid Sudoku solution



# Second Attempt

import numpy as np

def validSolution(board):
    n =len(board)
    board = np.array(board)
    digits = [i for i in range(1,10)]
    is_unique = lambda x: sorted(x) != digits
    if any([is_unique(b[i]) for i in range(n)]):
        return False  #rows, consist of digits 1-9
    if any([is_unique(b.T[i]) for i in range(n)]):
        return False  # cols, consist of digits 1-9
    for row in [3,6,9]: # each sub 3x3 grid consists of digits 1-9
        for col in [3,6,9]:
            if is_unique([board[i][j] for i in range(row-3,row) for j in range(col-3,col)]):
                return False
    return True

# First Attempt, obviously can be made more efficient

def validSolution(b):
    n =len(b)
    for i in range(n):
        t = sorted(b[i])
        if t != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for j in range(n):
        for i in range(n):
            a.append(b[i][j])
        u = sorted(a)
        if u != [1,2,3,4,5,6,7,8,9]:
            return False
        a = []
    for i in range(3):
        for j in range(3):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(3,6):
        for j in range(3,6):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(6,9):
        for j in range(6,9):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(3):
        for j in range(3,6):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(3):
        for j in range(6,9):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(3,6):
        for j in range(3):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(3,6):
        for j in range(6,9):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(6,9):
        for j in range(3):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    a = []
    for i in range(6,9):
        for j in range(3,6):
            a.append(b[i][j])
    u = sorted(a)
    if u != [1,2,3,4,5,6,7,8,9]:
            return False
    return True