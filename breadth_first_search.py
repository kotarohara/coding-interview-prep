# Code from the following page:
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs(graph, start):
    visited, queue = set(), [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print node
            visited.add(node)
            queue.extend(graph[node] - visited)


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        visited.add(node)
        for next in graph[node] - set(visited):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

if __name__ == "__main__":
    print list(bfs_paths(graph, "A", "F"))
