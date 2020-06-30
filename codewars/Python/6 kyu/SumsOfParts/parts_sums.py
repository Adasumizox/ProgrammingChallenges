def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result