from scipy.io import loadmat
import scipy.io as scio
import linecache
import numpy as np

def read_feateure(feature, fea_size):
    leftA = np.zeros([fea_size, 1])

    for i in range(0, fea_size):
        leftA[i, 0] = i
    newA = np.hstack((leftA, feature))
    np.savetxt('./data/facebook/features.txt', newA, delimiter=' ', fmt='%d')


if __name__=='__main__':
    datadiv = 'facebook'
    data = loadmat('./data/' + datadiv+ '.mat')
    # data = loadmat('./data/'+ datadiv +'/' + datadiv+ '.mat')
    value = data['Attributes']
    print(value)
    feature=np.array(value)
    print(feature.shape)
    fea_size = feature.shape[0]
    read_feateure(feature, fea_size)

