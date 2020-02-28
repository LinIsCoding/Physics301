import argparse
from numpy import sin 
from math import pi 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np

'''
Call signature:
    > python HW3_plot.py -x1 40 -x2 40
'''

def antisym(x1, x2, n1=1, n2=2, a=1.):
    '''
    This function takes two parameters
    Then plot two functions side by side
    '''
    y1 = lambda x1, x2: (2./a) * (sin((n1*pi*x1)/a)*sin((n2*pi*x2)/a) - sin((n1*pi*x2)/a)*sin((n2*pi*x1)/a))
    y2 = lambda x1, x2: ((2./a) * (sin((n1*pi*x1)/a)*sin((n2*pi*x2)/a) - sin((n1*pi*x2)/a)*sin((n2*pi*x1)/a)))**2
    
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), subplot_kw={'projection': '3d'})
    fig.suptitle('Antisymmetric Spatial Wave Function')
    
    # The first plot
    x1_range = np.linspace(0., a, x1)
    x2_range = np.linspace(0., a, x2)
    X1, Y1 = np.meshgrid(x1_range, x2_range)
    Z1 = y1(X1, Y1)
    axes[0].plot_surface(X1, Y1, Z1, rstride=1, cstride=1, linewidth=0, cmap=cm.coolwarm, antialiased=False)
    axes[0].set_title('Wave Function')

    # The second plot
    Z2 = y2(X1, Y1)
    axes[1].plot_surface(X1, Y1, Z2, rstride = 2, cstride = 2, cmap=cm.coolwarm, linewidth = 0)
    axes[1].set_title('Probability Density')

    fig.text(0.1,0.01, 'The "effective" interaction between two neutral Fermions (both spin up) that arises from the symmetry requirement on the total wave function.')
    plt.show()





if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-x1', type = int)
    parser.add_argument('-x2', type = int)

    args = parser.parse_args()

    x1 = args.x1
    x2 = args.x2
    antisym(x1, x2)