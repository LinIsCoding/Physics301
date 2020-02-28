import argparse
import numpy as np

'''
Call signature:
    > python HW3_prime.py -num1 2 -num2 9 
'''
def is_prime(n):
    '''
    This function is a helper function to determine a prime number
    '''
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def find_prime(x, y):
    '''
    This function finds all prime numbers between two given numbers
    '''
    if x > y or y <= 1:
        print('No prime numbers between {:d} and {:d}'.format(x, y))
        return
    if x <= 1:
        x = 2
    list = [n for n in np.arange(x, y + 1, 1) if is_prime(n)]
    print(list)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-num1', type = int)
    parser.add_argument('-num2', type = int)

    args = parser.parse_args()

    num1 = args.num1
    num2 = args.num2
    find_prime(num1, num2)
