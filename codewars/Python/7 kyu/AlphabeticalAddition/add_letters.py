def add_letters(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)