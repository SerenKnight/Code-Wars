def solution(roman):
    count = 0
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman)):
        if my_dict[roman[i]] > my_dict[roman[i + 1]]:
            count += i
        else:
            pass
    print(count)


solution("XXI")
