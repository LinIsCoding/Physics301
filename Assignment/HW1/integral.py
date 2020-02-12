'''
    The funtion computes the integral.
    Accumulate areas together to get the result.

    >>> intg(f1, 0, math.pi,1e-7,False)
    (1.9999999842068952, 2.5261390401347354e-08)
    >>> intg(f2, 1, 3,1e-7,False)
    (0.31809239176326926, 5.960471005492199e-08)
'''

import math
def intg(f, xlo, xhi, tol = 1e-7, print_progress = True):
    interval = 1.
    pre_integral = 0.
    diff = float("inf")

    if print_progress:
        print("running...")

    while (diff >= tol):
        # compute the number of steps
        steps = int((xhi - xlo) / interval)
        v_list = [xlo + interval * i for i in range(steps)]
        integral = 0.

        # accumulate areas
        for v in v_list:
            integral += f(v) * interval
        diff = abs(integral - pre_integral)/integral

        if print_progress:
            print('number of steps:{:5d}'.format(steps))
            print('dy = {:0.5f}, integral = {:0.8f}'.format(interval, integral))
            if interval - 1. == 0.:
                print("frac_diff = N/A")
            else:
                print('frac_diff = {:0.8f}%'.format(diff * 100.))
        # update data
        pre_integral = integral
        interval /= 2
    return integral, diff

def print_output(tuple):
    integral = tuple[0]
    diff = tuple[1]
    print('The integral evaluated to within specified accuracy: {:0.8f}'.format(integral))
    print('The upper limit of its fractional error is estimated to be: {:0.8f}'.format(diff))
    print('The correct answer is: {:0.8f}'.format(math.pi**4 / 15))
    print('The actual fractional error is: {:0.8f}%'.format(abs(diff - (1e-7)) * 100.))

if __name__ == "__main__":

    f1 = lambda x: math.sin(x)
    f2 = lambda x: math.e**(-x)
    f3 = lambda x: (x**3) / (math.e**x - 1) if x != 0 else 0
    t = intg(f3, 0, 100)
    print_output(t)
    import doctest
    doctest.testmod()