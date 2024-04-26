def compare(perm1, perm2):
    matrix1 = generate_matrix(perm1)
    matrix2 = generate_matrix(perm2)
    n = len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] > matrix2[i][j]:
                return False
    return True

def calculate_element(r_matrix, i, j):
    n = len(r_matrix)
    el = 0
    for k in range(n):
        for l in range(n):
            if k >= i and l <= j and r_matrix[k][l] == '.':
                el += 1
    return el

def generate_matrix(perm1):
    n = len(perm1)
    square = [['' for _ in range(n)] for _ in range(n)]
    for idx, el in zip(list(range(n)), perm1):
        square[el - 1][idx] = '.'
    r_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            r_matrix[i][j] = calculate_element(square, i, j)
    return r_matrix