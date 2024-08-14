def number_joy(n):
    factors = 0
    reversed_digits = ""
    for i in range(len(str(n))):
        factors += int(str(n)[i])
    if n % factors == 0:
        for j in range(len(str(factors))):
            reversed_digits += str(factors)[-(j + 1)]
        if factors * int(reversed_digits) == n:
            return True
        else:
            return False
    else:
        return False


print(number_joy(1729))
