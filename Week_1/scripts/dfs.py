from graph import *

def dfs(graph, start, end):
    visited = []
    frontier = []

    # Them node start vao frontier va visited
    frontier.append(start)
    visited.append(start)

    # start khong co node cha
    parent = dict()
    parent[start] = None

    path_found = False
    while True:
        if frontier == []:
            raise Exception("No path found")
        current_node = frontier.pop()
        visited.append(current_node)

        # Kiem tra current_node co la node end khong
        if current_node == end:
            path_found = True
            break

        for node in graph[current_node]:
            if node not in visited:
                frontier.append(node)
                parent[node] = current_node
                visited.append(node)
    
    # Xay dung duong di
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    
    return path