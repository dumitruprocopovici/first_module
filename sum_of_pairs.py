def sum_pairs(ints, s):
    tuple(ints)
    repeated_elements = []
    for i in ints:
        if i not in repeated_elements or i == s / 2:
            repeated_elements.append(i)
    tuple(repeated_elements)
    print(repeated_elements)
    for i in range(1, len(repeated_elements)):
        for j in range(i):
            if repeated_elements[i] + repeated_elements[j] == s:
                return [repeated_elements[j], repeated_elements[i]]


print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
