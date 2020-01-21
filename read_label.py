import numpy as np

def read_label(label):
    print(label)
    print("len(lines)")
    dataMat = np.zeros([len(label), 2])
    i = 0
    for l in label:
        dataMat[i, 0] = i
        dataMat[i, 1] = l
        i = i + 1
        # L = label.split(' ')
    print(dataMat)


    np.savetxt('./data/facebook/group.txt', dataMat, delimiter=' ', fmt='%d')

if __name__ == "__main__":
    label = np.loadtxt('./data/facebook.group')
    read_label(label)