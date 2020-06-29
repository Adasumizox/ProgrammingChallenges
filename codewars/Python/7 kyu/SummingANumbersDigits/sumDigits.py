def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))