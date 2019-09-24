from math import ceil
def who_is_next(names, r):
    while r > len(names):
        r = ceil((r - len(names)) / 2)
    return names[int(r-1)]