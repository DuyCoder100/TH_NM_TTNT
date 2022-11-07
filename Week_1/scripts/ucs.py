from graph import *

def ucs(graph, start, end):
    visited = []
    frontier = PriorityQueue()

    # Them node start vao frontier va visited
    frontier.put((0, start))
    visited.append(start)

    # Node start khong co node cha
    parent = dict()
    parent[start] = None

    path_found = False
    while True:
        if frontier.empty():
            raise Exception("No path found")
        current_weight, current_node = frontier.get()
        visited.append(current_node)

        # Kiem tra current_node co la node end khong
        if current_node == end:
            path_found = True
            break

        for node_i in graph[current_node]:
            node, weight = node_i
            if node not in visited:
                frontier.put((current_weight + weight, node))
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
    
    return current_weight, path