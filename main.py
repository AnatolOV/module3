def get_matrix(n, m, value):
    matrix = []
    for el in range(n):
        matrix.append([])
        for e in range(m):
            matrix[el].append(value)
    return matrix

print(get_matrix(3, 5 ,42))
