def unique_in_order(sequence):
    listed_sequence = list(sequence)
    new_sequence = []

    for x in range(len(listed_sequence) - 1):
        if listed_sequence[x + 1] != listed_sequence[x]:
            new_sequence.append(listed_sequence[x])
    if listed_sequence != []:
        new_sequence.append(listed_sequence[-1])
    return new_sequence


unique_in_order("AAAABBBCCDAABBB")
