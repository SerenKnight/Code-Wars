def disemvowel(string):
    letters = []
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for letter in string:
        letters.append(letter)

    for vowel in vowels:
        if vowel in letters:
            for i in range(letters.count(vowel)):
                letters.remove(vowel)
    new_word = "".join(letters)
    return new_word


print(disemvowel("This website is for losers LOL!"))
