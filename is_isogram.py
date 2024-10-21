def is_isogram(string):
    letters = list(string.lower())
    for letter in letters:
        if letters.count(letter) > 1:
            return False
    if letters == []:
        return True
    return True
