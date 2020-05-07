'''
    > python pca_letters.py -let_idx 5 -n_comp 8
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy
import matplotlib.image as mpimg
from sklearn.decomposition import PCA
import argparse

# function to perform PCA on X
def alphabet_pca(X, n_comp=5):
    pca = PCA(n_comp)  
    Xproj = pca.fit_transform(X)
    pca_comps = pca.components_
    
    f, axes = plt.subplots(1, n_comp, figsize=(n_comp*2, 2), subplot_kw=dict(xticks=[], yticks=[]))
    for i in range(n_comp):
        axes[i].imshow(pca_comps[i].reshape((16, 16)), cmap='binary')
        
    return pca, Xproj, pca_comps

# function to construct data array for all 26 letters
def create_letter_arr():
    X = np.random.rand(26, 256)
    idx = 0

    A, A_flat = make_let_im('SciComp-HW07-images/letterA.png', edge_pix=138)
    X[idx] = A_flat
    idx += 1
    
    B, B_flat = make_let_im('SciComp-HW07-images/letterB.png', edge_pix=130)
    X[idx] = B_flat
    idx += 1
    
    C, C_flat = make_let_im('SciComp-HW07-images/letterC.png', edge_pix=129)
    X[idx] = C_flat
    idx += 1
    
    D, D_flat = make_let_im('SciComp-HW07-images/letterD.png', edge_pix=139)
    X[idx] = D_flat
    idx += 1
    
    E, E_flat = make_let_im('SciComp-HW07-images/letterE.png', edge_pix=120)
    X[idx] = E_flat
    idx += 1
    
    F, F_flat = make_let_im('SciComp-HW07-images/letterF.png', edge_pix=114)
    X[idx] = F_flat
    idx += 1
    
    G, G_flat = make_let_im('SciComp-HW07-images/letterG.png', edge_pix=149)
    X[idx] = G_flat
    idx += 1
    
    H, H_flat = make_let_im('SciComp-HW07-images/letterH.png', edge_pix=143)
    X[idx] = H_flat
    idx += 1
    
    I, I_flat = make_let_im('SciComp-HW07-images/letterI.png')
    X[idx] = I_flat
    idx += 1
    
    J, J_flat = make_let_im('SciComp-HW07-images/letterJ.png', edge_pix=86)
    X[idx] = J_flat
    idx += 1
    
    K, K_flat = make_let_im('SciComp-HW07-images/letterK.png', edge_pix=126)
    X[idx] = K_flat
    idx += 1
    
    L, L_flat = make_let_im('SciComp-HW07-images/letterL.png', edge_pix=106)
    X[idx] = L_flat
    idx += 1
    
    M, M_flat = make_let_im('SciComp-HW07-images/letterM.png', edge_pix=156)
    X[idx] = M_flat
    idx += 1
    
    N, N_flat = make_let_im('SciComp-HW07-images/letterN.png', edge_pix = 144)
    X[idx] = N_flat
    idx += 1
    
    O, O_flat = make_let_im('SciComp-HW07-images/letterO.png', edge_pix=151)
    X[idx] = O_flat
    idx += 1
    
    P, P_flat = make_let_im('SciComp-HW07-images/letterP.png', edge_pix=125)
    X[idx] = P_flat
    idx += 1
    
    Q, Q_flat = make_let_im('SciComp-HW07-images/letterQ.png', edge_pix=150)
    X[idx] = Q_flat
    idx += 1
    
    R, R_flat = make_let_im('SciComp-HW07-images/letterR.png', edge_pix=131)
    X[idx] = R_flat
    idx += 1
    
    S, S_flat = make_let_im('SciComp-HW07-images/letterS.png', edge_pix=114)
    X[idx] = S_flat
    idx += 1
    
    T, T_flat = make_let_im('SciComp-HW07-images/letterT.png', edge_pix=121)
    X[idx] = T_flat
    idx += 1
    
    U, U_flat = make_let_im('SciComp-HW07-images/letterU.png')
    X[idx] = U_flat
    idx += 1
    
    V, V_flat = make_let_im('SciComp-HW07-images/letterV.png', edge_pix=136)
    X[idx] = V_flat
    idx += 1
    
    W, W_flat = make_let_im('SciComp-HW07-images/letterW.png', edge_pix=196)
    X[idx] = W_flat
    idx += 1
    
    X_x, X_flat = make_let_im('SciComp-HW07-images/letterX.png', edge_pix=127)
    X[idx] = X_flat
    idx += 1
    
    Y, Y_flat = make_let_im('SciComp-HW07-images/letterY.png', edge_pix=120)
    X[idx] = Y_flat
    idx += 1
    
    Z, Z_flat = make_let_im('SciComp-HW07-images/letterZ.png', edge_pix=115)
    X[idx] = Z_flat

    return X

# function to prepare letter image data
def make_let_im(let_file, dim=16, y_lo=70, y_hi=220, x_lo=10, x_hi=200, edge_pix=148, plot_let=False):
    letter = mpimg.imread(let_file)
    im = letter[y_lo:y_hi, x_lo:x_hi, 0]
    im = im[:,:edge_pix]
    
    x = np.arange(0, im.shape[1], 1)
    y = np.arange(0, im.shape[0], 1)
    f = scipy.interpolate.interp2d(x, y, im)

    new_x = np.linspace(0, x.max(), dim)
    new_y = np.linspace(0, y.max(), dim)
    let_im = f(new_x, new_y)

    if plot_let:
        plt.figure(figsize=(4,4))
        plt.imshow(let_im, cmap='gray_r')
        plt.show()
        
    let_im_fla = []
    for arr in let_im:
        let_im_fla = np.concatenate((let_im_fla, arr))
        
    return let_im, let_im_fla

# function to reconstruct the letter
def show_pca_im(Xproj, pca_comps, dim=16, let_idx=0):
    dig_im_rec = np.zeros((dim, dim))
    coeffs = Xproj[let_idx]

    for i in range(pca_comps.shape[0]):
        dig_im_rec += coeffs[i]*pca_comps[i].reshape((dim, dim))
        
    plt.figure(figsize=(3,3))
    plt.axis('equal')
    plt.imshow(dig_im_rec, cmap='binary')
    plt.show()
    return dig_im_rec

# main function
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-let_idx', type = int)
    parser.add_argument('-n_comp', type = int)
    # get parameters
    args = parser.parse_args()
    let_idx = args.let_idx
    n_comp = args.n_comp

    X = create_letter_arr()
    alfbet_pca, Xproj, pca_comps = alphabet_pca(X, n_comp=n_comp)
    let_coef = show_pca_im(Xproj, pca_comps, let_idx=let_idx)
