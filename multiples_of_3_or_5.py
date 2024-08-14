def multiples(number):
    my_list = []
    if number < 0:
        return 0
    else:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                if i not in my_list:
                    my_list.append(i)
    print(my_list)
    return sum(my_list)


number = 50

print(multiples(number))
