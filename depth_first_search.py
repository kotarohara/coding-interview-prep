# Code from the following page:
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    stack, visited = [start], set()

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()
        for node in graph[vertex] - set(path):
            if node == goal:
                yield path + [node]
            else:
                stack.append((node, path + [node]))

if __name__ == "__main__":
    print list(dfs_paths(graph, "A", "F"))
