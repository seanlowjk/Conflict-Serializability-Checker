def permutations(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    temp = []

    for i in range(len(lst)):
        curr = lst[i]
        remainder = lst[:i] + lst[i + 1 :]
        for p in permutations(remainder):
            temp.append([curr] + p)
    return temp
