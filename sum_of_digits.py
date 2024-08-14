def get_sum_of_digits(num):
    count = 0
    digits = str(num)
    numbers = list(digits)
    for i in numbers:
        count += int(i)
    return count


print(get_sum_of_digits(123))
