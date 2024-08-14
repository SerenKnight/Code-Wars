def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
