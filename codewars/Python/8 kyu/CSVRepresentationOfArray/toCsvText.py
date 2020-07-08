def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)