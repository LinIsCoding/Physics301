import matplotlib.image as mpimg
from sklearn.datasets import load_digits

import sys
sys.path.insert(0, '../pattern_recog_func')
from pattern_recog_func import interpol_im
from pattern_recog_func import pca_svm_pred
from pattern_recog_func import pca_X
from pattern_recog_func import rescale_pixel
from pattern_recog_func import svm_train

# part a
def train_and_validate():
    # load data
    raw_data = load_digits()
    X = raw_data.data
    y = raw_data.target

    # organize data
    X_train = X[:60]
    y_train = y[:60]

    X_valid = X[60:80]
    y_valid = y[60:80]

    # train and validate
    md_clf = svm_train(X_train, y_train)
    y_pred = md_clf.predict(X_valid)

    # check the result
    idx = [i for i in range(len(y_pred)) if y_valid[i] != y_pred[i]]
    for i in idx:
        print("index, actual digit, svm_prediction: {:d} {:d} {:d}".format(i + 60, y_valid[i], y_pred[i]))
        
    precision = (20 - len(idx))/20
    print("Total number of mid-identifications: {:d}".format(len(idx)))
    print("Success rate: {:.2f}".format(precision))
    
    return md_clf

# part b
def test_pred(md_clf):
    unseen = mpimg.imread("unseen_dig.png")
    unseen = interpol_im(unseen, plot_new_im=True)
    unseen = rescale_pixel(unseen)
    result = md_clf.predict(unseen.reshape(1, -1))
    print("The prediction: ", result[0])

# part c
def pred_on_pca():
    # load data
    raw_data = load_digits()
    X = raw_data.data
    y = raw_data.target

    # organize data
    X_train = X[:60]
    y_train = y[:60]

    X_valid = X[60:80]
    y_valid = y[60:80]

    # train
    pca, X_proj = pca_X(X_train, n_comp=30)
    md_clf_new = svm_train(X_proj, y_train)

    # validate
    file = "unseen_dig.png"
    prediction = pca_svm_pred(file, pca, md_clf_new)
    print("The prediction: ", prediction[0])

# main function
if __name__ == '__main__':
    print("--- part a ---")
    md_clf = train_and_validate()
    print("--- part b ---")
    test_pred(md_clf)
    print("--- part c ---")
    pred_on_pca()
   