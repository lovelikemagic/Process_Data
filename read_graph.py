import numpy as np
import linecache

def read_graph(graph):
    lines = linecache.getlines(graph)
    lines = [line.rstrip('\n') for line in lines]
    print("len(lines)")
    dataMat=[]
    # dataMat = np.zeros([len(graph), 2])
    for l in lines:
        line = l.split('\t')
        dataMat.append(line)
        # dataMat[i, 0] = i
        # dataMat[i, 1] = l
        # i = i + 1
        # L = label.split(' ')
    print(dataMat)


    np.savetxt('./data/facebook/edges.txt', dataMat, delimiter=' ', fmt = '%s')

if __name__ == "__main__":
    graph = './data/facebook.edgelist'
    read_graph(graph)