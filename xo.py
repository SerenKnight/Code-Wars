def xo(s):
    count_x = 0
    count_o = 0

    x = list(s)
    for item in x:
        if x == "x" or "X":
            count_x += 1
        elif x == "o" or "O":
            count_o += 1
    if count_x == count_o:
        return True
    else:
        return False
