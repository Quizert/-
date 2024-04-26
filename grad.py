def find_min_vertex(adj_matrix):
    n = len(adj_matrix)
    # Минимальная вершина: нет входящих рёбер
    for j in range(n):
        if all(adj_matrix[i][j] == 0 for i in range(n) if i != j):
            return j
    return None

def find_max_vertex(adj_matrix):
    n = len(adj_matrix)
    # Максимальная вершина: нет исходящих рёбер
    for i in range(n):
        if all(adj_matrix[i][j] == 0 for j in range(n) if i != j):
            return i
    return None

def dfs_paths(adj_matrix, current_vertex, end_vertex, path, all_paths, visited):
    path.append(current_vertex)
    visited[current_vertex] = True
    if current_vertex == end_vertex:
        all_paths.append(list(path))
    else:
        for j in range(len(adj_matrix)):
            if adj_matrix[current_vertex][j] == 1 and not visited[j]:
                dfs_paths(adj_matrix, j, end_vertex, path, all_paths, visited)
    path.pop()
    visited[current_vertex] = False

def check_paths(adj_matrix):
    start_vertex = find_min_vertex(adj_matrix)
    end_vertex = find_max_vertex(adj_matrix)
    if start_vertex is None or end_vertex is None:
        return False, "Нет минимальной или максимальной вершины."
    
    all_paths = []
    path = []
    visited = [False] * len(adj_matrix)
    
    dfs_paths(adj_matrix, start_vertex, end_vertex, path, all_paths, visited)
    
    if not all_paths:
        return False, "Пути от минимальной к максимальной вершины не найдены."

    # Проверяем, что все пути имеют одинаковую длину
    path_length = len(all_paths[0])
    if all(len(p) == path_length for p in all_paths):
        return True, path_length
    else:
        return False
