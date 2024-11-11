def array_diff(a, b):
    output = []
    for x in a:
        if x not in b:
            output.append(x)
    return output


print(array_diff([1, 2, 2, 2, 3], [2]))
