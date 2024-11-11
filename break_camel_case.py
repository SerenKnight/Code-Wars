def breakcamelcase(camelCase):
    output = ""
    for letter in camelCase:
        if letter.islower():
            output += letter
        else:
            output += " " + letter.upper()
    return output


print(breakcamelcase("camelCasing"))
