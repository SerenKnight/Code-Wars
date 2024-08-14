def descending_order(num):
    step_one = str(num)
    step_two = list(step_one)
    step_two.sort()
    step_two.reverse()
    x = "".join(e for e in step_two)
    return int(x)


descending_order(6136271)
