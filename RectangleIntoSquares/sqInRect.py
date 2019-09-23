def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)