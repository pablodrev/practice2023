graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': []
}
start = 'A'
end = 'F'


def find_path(graph, start, end, parents):
    if end in graph[start]:
        parents += [end]
        print(" - ".join(parents))
        parents.clear()
        return
    elif len(graph[start]) == 0:
        return
    else:
        neighbors = graph[start]
        for n in neighbors:
            find_path(graph, n, end, parents + [n])


find_path(graph, start, end, [start])
