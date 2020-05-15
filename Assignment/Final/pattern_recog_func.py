import numpy as np
import matplotlib.pyplot as plt
import scipy
import matplotlib.image as mpimg
from sklearn.decomposition import PCA
from sklearn import svm
from copy import copy

# function to interpolate the input image
def interpol_im(im, dim1=8, dim2=8, plot_new_im=False, cmap='binary', grid_off=False):
    image = copy(im[:, :, 0])

    # interpolate
    x = np.arange(0, image.shape[0], 1)
    y = np.arange(0, image.shape[1], 1)
    f = scipy.interpolate.interp2d(y, x, image)

    new_x = np.linspace(0, x.max(), dim1)
    new_y = np.linspace(0, y.max(), dim2)
    new_im = f(new_x, new_y)
    
    # plot the image
    if plot_new_im:
        plt.figure(figsize=(4,4))
        plt.imshow(new_im, cmap=cmap, interpolation='nearest')
        plt.title("image")
        if grid_off:
            plt.grid('off')
        plt.show()

    # generate 1D array   
    flatten_im = []
    for arr in new_im:
        flatten_im = np.concatenate((flatten_im, arr))
    
    return flatten_im

# function to predict based on PCA space
def pca_svm_pred(imfile, md_pca, md_clf, dim1=45, dim2=60):
    im = mpimg.imread(imfile)
    im = interpol_im(im)
    im = rescale_pixel(im)
    
    X_proj = md_pca.transform(im.reshape(1, -1))
    y_pred = md_clf.predict(X_proj)
    
    return y_pred

# function to create PCA object and projections
def pca_X(X, n_comp=10):
    pca = PCA(n_components=n_comp, whiten=True)  
    Xproj = pca.fit_transform(X)
    return pca, Xproj

# function to rescale the pixel value of the image
def rescale_pixel(unseen):
    im = copy(unseen)    
    im = 1.0 - im
    im *= 16
    im = im.astype(int)
    return im

# function to train model
def svm_train(X, y, gamma=0.001, C=100):
    clf = svm.SVC(gamma=gamma, C=C)
    clf.fit(X, y)
    return clf
