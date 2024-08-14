def flatten(lst):
    new_list = []
    for i in range(len(lst)):
        try:
            for j in range(len(lst[i])):
                new_list.append(lst[i][j])
        except:
            new_list.append(lst[i])
    print(new_list)


flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]])
