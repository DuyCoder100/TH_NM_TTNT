from graph import *

def bfs(graph, start, end):
    visited = []
    frontier = Queue()

    # Them node start vao frontier va visited
    frontier.put(start)
    visited.append(start)

    # Node start khong co node cha
    parent = dict()
    parent[start] = None

    path_found = False

    while True:
        if frontier.empty():
            raise Exception("No path found")
        current_node = frontier.get()
        visited.append(current_node)

        # Kiem tra current_node co la node end khong
        if current_node == end:
            path_found = True
            break

        for node in graph[current_node]:
            if node not in visited:
                frontier.put(node)
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