import doctest
import argparse
import math
import sys
sys.path.insert(0, '../HW1')
from integral import intg
import pdb

'''
    Call signature:
    
    > python HW2_2.py -t 2. -tol 1e-4
    
    To run doctests:

    > python -m doctest HW2_2.py
    
    Verbose mode:
    
    > python -m doctest -v HW2_2.py
'''

def factorial(t):
    '''
    factorial is called when input is an integer
    It generates result based on formula (t - 1)!

    >>> factorial(4)
    6

    >>> factorial(5)
    24
    '''

    res = 1
    for x in range(1, t):
        res *= x
    return res
    

def gamma(t, tol=1e-4):
    '''
    gamma is called when input is a float
    It generates result based on integral

    >>> abs(1. - round(gamma(2.0)[0], 3)) / 1. < 1e-4
    True

    >>> abs(0.887 - round(gamma(1.4)[0], 3)) / 0.887 < 1e-4
    True

    >>> abs(0.946 - round(gamma(1.85)[0], 3)) / 0.946 < 1e-4
    True
    '''

    if t < 1. or t > 100. :
        print("Please enter a number between 1 and 100(inclusive).")
        return
    f = lambda x: (x**(t-1)) * (math.e**(-x))
    return intg(f, 0., 1000., tol, print_progress=False) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # take two arguments from command line
    parser.add_argument('-t', type = float)
    parser.add_argument('-tol', type = float)

    # get parameters
    args = parser.parse_args()
    t = args.t
    tol = args.tol

    # call funtion
    if type(t) == int:
        res = factorial(t)
        print('The result is {:d}\n'.format(res))
    else :
        integral, diff = gamma(t, tol)
        print('The final integral is {:0.8f}, and the fractional difference is {:0.8f}'.format(integral, diff))
