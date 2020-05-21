import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import argparse

'''
    > python FourierDescriptor.py -order 10 --no-norm -zeroth
    > python FourierDescriptor.py -order 10
'''
def extract_shape(im_file, blowup=1., plot_img=False, plot_contour=False, plot_contour_pts=False):
    im = mpimg.imread(im_file)
    im = im[:, :, 0]
    
    if plot_img:
        plt.figure()
        plt.title('Original Shape')
        plt.imshow(im, cmap = plt.cm.gray)

    x = np.arange(im.T.shape[0])*blowup  
    y = np.arange(im.T.shape[1])*blowup
    X, Y = np.meshgrid(x, y)
    
    plt.figure(figsize = (10, 10))
    plt.axis('equal')
    plt.title('Contours')
    
    CS = plt.contour(X, Y, im, 1)
    levels = CS.levels
    if not plot_contour:
        plt.close()

    cs_paths = CS.collections[0].get_paths()
    x_arr = []
    y_arr = []
    for p in cs_paths:
        v = p.vertices
        x_arr.append(v[:,0])
        y_arr.append(v[:,1])
    
    if plot_contour_pts:
        plt.figure()
        plt.title("Verify the contour points are correct")
        plt.plot(x_arr, y_arr)
        
    if plot_img or plot_contour or plot_contour_pts:
        plt.show()
    return x_arr, y_arr

def FD(x, y, plot_FD=False, y_lim=None):
    N = len(x)
    z = x + y*1j
    z_rot = z * np.e**(1j*4*np.pi)
    Z = np.fft.fft(z_rot)
        
    d_complex = np.gradient(z_rot)
    d = np.abs(d_complex).mean()
       
    k = np.fft.fftfreq(len(z), d = d)
    k_lo = np.abs(k[np.argsort(np.abs(k))][1])

    if plot_FD:
        plt.figure()
        plt.title('FD real')
        plt.plot(k, Z.real, 'b.')
        plt.xlabel('k')
        plt.ylabel('Re[FD]')
        if y_lim != None:
            plt.ylim([-y_lim, y_lim])
            
        plt.figure()
        plt.title('FD imag')
        plt.plot(k, Z.imag, 'g.')
        plt.xlabel('k')
        plt.ylabel('Im[FD]')
        if y_lim != None:
            plt.ylim([-y_lim, y_lim])
        plt.show()
    return Z, k, k_lo

def filt_FD(Z, n_keep, no_zeroth=True):
    f_filt = np.zeros(len(Z))
    f_filt[1:n_keep + 1] = 1
    f_filt[len(Z) - n_keep - 1:] = 1
    if not no_zeroth:
        f_filt[0] = 1
    return Z*f_filt

def get_FD_abs(x, y, order=10, norm=True, no_zeroth=True):
    Z, k, k_lo = FD(x, y)
    
    N = len(x)
    Z_filt = filt_FD(Z, order, no_zeroth)
    
    if norm:
        Z_filt = size_norm(Z_filt)
        
    x_rec, y_rec = recover_shape(Z_filt)
    fd_mag = np.abs(Z_filt)
    k_kept = k

    # throw away zero terms
    if no_zeroth:
        fd_mag = np.abs(Z_filt[Z_filt != 0])
        k_kept = k[Z_filt != 0]
    return fd_mag, k_kept, x_rec, y_rec

def recover_shape(Z):
    z_rec = np.fft.ifft(Z)
    x_rec = z_rec.real
    y_rec = z_rec.imag
    return x_rec, y_rec

def size_norm(Z):
    return Z/np.sqrt(np.abs(Z[1])*np.abs(Z[-1]))

def plot(y1, x1, y2, x2, y6_1, x6_1, y6_2, x6_2):
    fig = plt.figure()
    plt.title('Numbers Recovered From FD\'s')
    plt.plot(y1, x1, 'b')
    plt.plot(y2, x2, 'g')
    plt.plot(y6_1, x6_1, 'r')
    plt.plot(y6_2, x6_2, 'r')
    fig.savefig('rec_numbers126.pdf')
    plt.show()

def plot_mag(k1, fd1, k2, fd2, k6_1, fd6_1, k6_2, fd6_2):
    fig = plt.figure()
    plt.title('Magnitudes of FD\' for 1, 2 and 6')
    plt.plot(k1, fd1, 'b.')
    plt.plot(k2, fd2, 'gx')
    plt.plot(k6_1, fd6_1, 'r^')
    plt.plot(k6_2, fd6_2, 'r^')
    fig.savefig('FourierDescriptor_numbers126.pdf')
    plt.show()
    
def driver(order, norm, no_zeroth):
    x1, y1 = extract_shape('number1.png',blowup=1)
    x2, y2 = extract_shape('number2.png',blowup=1)
    x6, y6 = extract_shape('number6.png',blowup=1)

    fd1, k_kept1, x_rec1, y_rec1 = get_FD_abs(x1[0], y1[0], order=order, norm=norm, no_zeroth=no_zeroth)
    fd2, k_kept2, x_rec2, y_rec2 = get_FD_abs(x2[0], y2[0], order=order, norm=norm, no_zeroth=no_zeroth)
    fd6, k_kept6, x_rec6, y_rec6 = get_FD_abs(x6[0], y6[0], order=order, norm=norm, no_zeroth=no_zeroth)
    fd6_2, k_kept6_2, x_rec6_2, y_rec6_2 = get_FD_abs(x6[1], y6[1], order=order, norm=norm, no_zeroth=no_zeroth)


    plot(y_rec1, x_rec1, y_rec2, x_rec2, y_rec6, x_rec6, y_rec6_2, x_rec6_2)
    plot_mag(k_kept1, fd1, k_kept2, fd2, k_kept6, fd6, k_kept6_2, fd6_2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # take two arguments from command line
    parser.add_argument('-order', type = int)
    parser.add_argument('--no-norm', dest='norm', action='store_false')
    parser.add_argument('-zeroth', dest='no_zeroth', action='store_false') 
    parser.set_defaults(no_zeroth=True, norm=True)

    # get parameters
    args = parser.parse_args()
    order = 10
    norm = args.norm
    no_zeroth = args.no_zeroth

    # call funtion
    driver(order, norm, no_zeroth)