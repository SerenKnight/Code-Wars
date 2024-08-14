def remov_nb(n):
    product = int(1 / 2 * (n * (n + 1)))
    solutions = []
    for i in range(1, n + 1):
        j = int((product - i) / (1 + i))
        if j <= n:
            if product == (i * j) + i + j:
                sol = (i, j)
                solutions.append(sol)
    return solutions


print(remov_nb(26))
