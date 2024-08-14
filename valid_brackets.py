def valid_brackets(case):
    open_brackets = 0
    closed_brackets = 0
    last_bracket = ""
    for i in case:
        if len(case) == 0:
            return True
        elif len(case) == 1:
            return False
        else:
            if i == "(":
                open_brackets += 1
                last_bracket = "("
            elif i == ")":
                closed_brackets += 1
                last_bracket = ")"
    if open_brackets == closed_brackets:
        return True
    else:
        return False


case = "hi())("

print(valid_brackets(case))
