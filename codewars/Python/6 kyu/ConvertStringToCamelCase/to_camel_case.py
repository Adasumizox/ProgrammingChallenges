def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s