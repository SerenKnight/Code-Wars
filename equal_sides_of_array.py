def find_even_index(arr):
    sum_left = 0
    sum_right = 0
    for i in range(len(arr)):
        for j in range(i - 1, 0 - 1, -1):
            sum_left += arr[j]
        for k in range(i + 1, len(arr)):
            sum_right += arr[k]
        if sum_left == sum_right:
            return i
        sum_left = 0
        sum_right = 0
    return -1


arr = [1, 2, 3, 4, 3, 2, 1]

print(find_even_index(arr))
