def revrot(strng, sz):
    func = lambda x : x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1]
    return "" if sz <= 0 or sz > len(strng) else "".join(func(strng[i:i+sz]) for i in range(0, len(strng) - sz + 1, sz))