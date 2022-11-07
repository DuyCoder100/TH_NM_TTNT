from graph import *

# Doc du lieu tu file text
def read_txt(file):
    size = int(file.readline())
    start, goal = [int(num) for num in file.readline().split(' ')]
    matrix = [[int(num) for num in file.readline().split(' ')] for num in range(size)]
    return size, start, goal, matrix

# Chuyen ma tran thanh danh sach ke
def convert_graph(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                adjList[i].append(j)
    return adjList

def convert_graph_weight(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0:
                adjList[i].append((j, a[i][j]))
    return adjList