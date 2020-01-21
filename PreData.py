import numpy as np
import linecache
pathDir=''
def load_feature(feature_file,features_count):
    lines = linecache.getlines(feature_file)
    lines = [line.rstrip('\n') for line in lines]
    print("len(lines)")
    dataMat = np.zeros([len(lines), features_count])
    node_map = {}
    lable_map = []
    for idx, line in enumerate(lines):
        line = line.split('\t')
        i = 0
        for l in line:
            if i == 0:
                node_map[l] = idx
                dataMat[idx, i] = idx
            elif i == features_count:
                lable_map.append(l)
            else:
                dataMat[idx, i] = l
            i = i + 1
    labelMat = np.zeros([len(lines), 2])
    label = 0
    label_map = {}
    i = 0
    for label_name in lable_map:
        if label_name not in label_map:
            label = label + 1
            label_map[label_name] = label
        labelMat[i,1] = label_map[label_name]
        labelMat[i, 0] = i
        i = i + 1

    print(node_map)
    np.savetxt(pathDir+'group.txt', labelMat, delimiter=' ', fmt='%d')
    np.savetxt(pathDir+'features.txt', dataMat, delimiter=' ', fmt='%d')
    return node_map

def load_graph(graph_file,node_map):
    linesGraph = linecache.getlines(graph_file)
    linesG = [lineG.rstrip('\n') for lineG in linesGraph]
    print("len(linesG)")
    graphMat = np.zeros([len(linesG), 2])
    i = 0
    for line in linesG:
        arr = line.split(' ')
        graphMat[i, 0] = node_map[arr[0]]
        graphMat[i, 1] = node_map[arr[1]]
        i = i + 1
    np.savetxt(pathDir+'edges.txt', graphMat, delimiter=' ', fmt='%d')


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False
if __name__ == '__main__':
    dataName = "data"
    pathDir="./all/"+dataName+"/"

    mkdir(pathDir)
    graph_file = "./raw_data/WebKB/"+dataName+".cites"
    feature_file = "./raw_data/WebKB/"+dataName+".content"
    features_count=1704
    node_maps=load_feature(feature_file,features_count)
    graph_file = "./raw_data/WebKB/"+dataName+".cites"
    load_graph(graph_file,node_maps)


