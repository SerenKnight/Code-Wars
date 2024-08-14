def find_uniq(arr):
    for val in arr:
        if arr.count(val) > 1:
            continue
        else:
            return val


print(find_uniq([3, 10, 3, 3, 3]))
