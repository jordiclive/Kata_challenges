"""https://www.codewars.com/kata/5b5fe164b88263ad3d00250b/train/python, 3kyu"""


# A surprisingly Difficult Problem in Python

# A brute force first attempt solution, with parsimony with code length, shame about the run time..

import itertools
import re

Nos = [str(i) for i in range(10)]

def alphametics(crypt_input):
    def find_alpha_set(crypt_input):
        return list(set(re.findall(r"[a-zA-Z]",crypt_input))) # Extract letters from cryptogram

    def possible_dicts(crypt_input):  # Generate every combination of letter mapped to 0-9 possible, here efficiency can be gained
        letters = find_alpha_set(crypt_input) # by first removing combinations which map a beginning letter of a word to 0
        permutations = list(itertools.permutations(Nos, len(letters))) # obviously one needs to use generators, and yield and start with units to actually make efficient
        possible_dicts = [dict(zip(letters,comb)) for comb in permutations] # helps that problem only uses + operation
        return possible_dicts

    def evaluate(dict_,x): # evaluate the code mapping
        for key, value in dict_.items():
            x = x.replace(key,value)
        x = x.replace('=','==')
        return eval(x)

    possible_dicts = possible_dicts(crypt_input)  # again not very efficient, try & except for every single combination
    for possible in possible_dicts:
        try:
            if evaluate(possible,crypt_input):
                for key, value in possible.items():  # simple loop to produce first solution come across in required format
                        crypt_input = crypt_input.replace(key,value)
                return crypt_input
        except:
            continue
