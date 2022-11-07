from graph import *
from bfs import *
from dfs import *
from ucs import *
from utilities import *

if __name__ == '__main__':
    file_1 = open("Week_1/scripts/input.txt", "r")
    file_2 = open("Week_1/scripts/input_ucs.txt", "r")

    size_1, start_1, goal_1, matrix_1 = read_txt(file_1)
    size_2, start_2, goal_2, matrix_2 = read_txt(file_2)

    file_1.close()
    file_2.close()

    graph_1 = convert_graph(matrix_1)
    graph_2 = convert_graph_weight(matrix_2)

    result_bfs = bfs(graph_1, start_1, goal_1)
    print("Ket qua su dung thuat toan BFS:\n", result_bfs)

    result_dfs = dfs(graph_1, start_1, goal_1)
    print("Ket qua su dung thuat toan DFS:\n", result_dfs)

    cost, result_ucs = ucs(graph_2, start_2, goal_2)
    print("Ket qua su dung thuat toan UCS:\n", result_dfs, "\nTong chi phi la: ", cost)

    graph_new_1 = Graph()
    graph_new_1.read_file_text("Week_1/scripts/input.txt")
    adjList_1 = graph_new_1.convert_to_list()

    bfs_1_path = graph_new_1.bfs(graph_new_1.start_node, graph_new_1.end_node)
    print("BFS path: ", bfs_1_path)
    
    dfs_1_path = graph_new_1.dfs(graph_new_1.start_node, graph_new_1.end_node)
    print("DFS path: ", dfs_1_path)

    graph_new_2 = Graph()
    graph_new_2.read_file_text("Week_1/scripts/input_ucs.txt")
    adjList_2 = graph_new_2.convert_to_list(weight=True)

    ucs_2_path, ucs_2_min_weight = graph_new_2.ucs(graph_new_2.start_node, graph_new_2.end_node)
    print("UCS path: ", ucs_2_path, "\nwith min weight: ", ucs_2_min_weight)