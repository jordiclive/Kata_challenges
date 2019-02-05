"""Kata can be found at https://www.codewars.com/kata/catching-car-mileage-numbers/train/python, grade: 4kyu"""


def digit_followed_by_zeroes(number):
    s = str(number)
    for i in range(1,len(s)):
        if s[i] != '0':
            return False
    return True

def ispalindrome(number):  # Incorporates 'Every digit is the same number: eg. 1111'
    return str(number) == str(number)[::-1]

def isincrementing(number):
    return str(number) in '1234567890'  # number has to be in here as 0 is at end as question defines.

def isdecrementing(number):
    return str(number) in '9876543210'


criteria = (digit_followed_by_zeroes,ispalindrome,isincrementing,isdecrementing)
any_criteria_matches = lambda number: any(criterion(number) for criterion in criteria)

def is_interesting(number, awesome_phrases):
    if number in awesome_phrases:
        return 2
    if number > 99 and any_criteria_matches(number):
        return 2  # all possible 2 scoring cases
    if number+1 in awesome_phrases or number+2 in awesome_phrases:
        return 1
    if number > 97 and (any_criteria_matches(number+1) or any_criteria_matches(number+2)):
        return 1
    return 0