def add_neighbor(v, w, adjacency_list_by_vertex):
    if v == 'end' or w == 'start':
        return
    neighbors = adjacency_list_by_vertex.get(v)
    if neighbors is None:
        neighbors = []
        adjacency_list_by_vertex[v] = neighbors
    neighbors.append(w)


def is_small(v):
    return v.islower()


def dfs(v, adjacency_list_by_vertex, current_path, forbidden_vertices, paths):
    current_path.append(v)
    if v == 'end':
        paths.append(current_path[:])
    else:
        neighbors = adjacency_list_by_vertex.get(v)
        if neighbors is not None:
            if is_small(v):
                forbidden_vertices.add(v)
            for w in neighbors:
                if w not in forbidden_vertices:
                    dfs(w, adjacency_list_by_vertex, current_path, forbidden_vertices, paths)
            if is_small(v):
                forbidden_vertices.remove(v)
    current_path.pop()


def find_paths(adjacency_list_by_vertex):
    paths = []
    dfs('start', adjacency_list_by_vertex, [], set(), paths)
    return paths


def process(lines):

    adjacency_list_by_vertex = {}

    for line in lines:
        vertices = line.split('-')
        if len(vertices) >= 2:
            add_neighbor(vertices[0], vertices[1], adjacency_list_by_vertex)
            add_neighbor(vertices[1], vertices[0], adjacency_list_by_vertex)

    paths = find_paths(adjacency_list_by_vertex)

    return len(paths)


with open("/Users/viniciusgusmao/Documents/AoC2021/12test.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    print process(lines)
