def duplicate_count(text):
    count = 0
    completed_characters = []
    for i in range(len(text)):
        for j in range(len(text)):
            if (
                text[i].lower() == text[j].lower()
                and i != j
                and text[i].lower() not in completed_characters
            ):
                count += 1
                completed_characters.append(text[i].lower())
    return count


print(duplicate_count("aAbc"))
