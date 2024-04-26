def floyd_warshall_path_recovery(n, adj):
    # Матрица предшественников
    next_node = [[None if adj[i][j] == 0 and i != j else j for j in range(n)] for i in range(n)]
    
    # Инициализация путей
    for i in range(n):
        for j in range(n):
            if i != j and adj[i][j] == 0:
                adj[i][j] = float('-inf')

    # Алгоритм Флойда-Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] + adj[k][j] > adj[i][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]
                    next_node[i][j] = next_node[i][k]
    
    return next_node

def reconstruct_path(i, j, next_node):
    if next_node[i][j] is None:
        return False
    
    path = []
    intermediate = i
    while intermediate is not None and intermediate != j:
        path.append(intermediate)
        intermediate = next_node[intermediate][j]
        if intermediate in path:  # Это предотвращает зацикливание
            return False
    if intermediate is None:  # Проверка, что следующий шаг возможен
        return False
    path.append(j)
    return path

def mobius_func(adj_matrix):
    n = len(adj_matrix)
    next_node = floyd_warshall_path_recovery(n, adj_matrix)
    matrix_of_path = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_of_path[i][j] = reconstruct_path(i, j, next_node)

    mu = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        mu[i][i] = 1

    for i in range(n):
        for j in range(n):
            if matrix_of_path[i][j] != False and i != j:
                s = 0
                path = matrix_of_path[i][j]
                for k in path:
                    s += mu[i][k]
                mu[i][j] = -s
    return mu