def sum_dig_pow(a, b):
    count = 0
    my_list = []
    for i in range(a, b + 1):
        if range(len(str(i))) == 0:
            pass
        else:
            for j in range(len(str(i))):
                count += int(str(i)[j]) ** (j + 1)
            if count == i:
                my_list.append(i)
            count = 0
    print(my_list)


sum_dig_pow(300, 598)
