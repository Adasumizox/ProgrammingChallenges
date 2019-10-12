def validate(n):
    digits = [int(x) for x in str(n)]
    for x in range(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))
    return sum(digits) % 10 == 0