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


def dfs(v, adjacency_list_by_vertex, current_path, forbidden_vertices, paths, small_forced_twice):
    current_path.append(v)
    if v == 'end':
        if small_forced_twice is None or current_path.count(small_forced_twice) == 2:
            paths.append(','.join(current_path[:]))
    else:
        neighbors = adjacency_list_by_vertex.get(v)
        if neighbors is not None:
            if is_small(v):
                if v == small_forced_twice and v.upper() not in forbidden_vertices:
                    v = v.upper()
                forbidden_vertices.add(v)
            for w in neighbors:
                if w not in forbidden_vertices:
                    dfs(w, adjacency_list_by_vertex, current_path, forbidden_vertices, paths, small_forced_twice)
            if v in forbidden_vertices:
                forbidden_vertices.remove(v)
    current_path.pop()


def find_paths(adjacency_list_by_vertex, small_forced_twice=None):
    paths = []
    dfs('start', adjacency_list_by_vertex, [], set(), paths, small_forced_twice)
    return len(paths)


def process(lines):

    adjacency_list_by_vertex = {}
    small_vertices_set = set()

    for line in lines:
        vertices = line.split('-')
        if len(vertices) >= 2:
            add_neighbor(vertices[0], vertices[1], adjacency_list_by_vertex)
            add_neighbor(vertices[1], vertices[0], adjacency_list_by_vertex)
            if is_small(vertices[0]):
                small_vertices_set.add(vertices[0])
            if is_small(vertices[1]):
                small_vertices_set.add(vertices[1])

    small_vertices_list = list(small_vertices_set)

    paths = find_paths(adjacency_list_by_vertex)

    for small_vertex in small_vertices_list:
        paths += find_paths(adjacency_list_by_vertex, small_vertex)

    return paths


with open("/Users/viniciusgusmao/Documents/AoC2021/12.txt") as file:
    matrix = []
    lines = file.read().split('\n')
    print process(lines)
