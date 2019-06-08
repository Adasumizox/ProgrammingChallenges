def snail(array):
    return list(array[0]) + snail(list(zip(*array[1:]))[::-1]) if array else []