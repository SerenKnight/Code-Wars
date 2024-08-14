def solution(roman):
    count = 0
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(roman) == 1:
        count += my_dict[roman[0]]
    elif len(roman) == 2:
        if my_dict[roman[-2]] >= my_dict[roman[-1]]:
            count += my_dict[roman[-2]] + my_dict[roman[-1]]
        else:
            count += my_dict[roman[-1]] - my_dict[roman[-2]]
    else:
        count += my_dict[roman[-1]]
        for i in range(len(roman) - 1):
            if my_dict[roman[-i - 2]] >= my_dict[roman[-i - 1]]:
                count += my_dict[roman[-i - 2]]
            else:
                count -= my_dict[roman[-i - 2]]
    print(count)


solution("MMCLXXXVIII")
