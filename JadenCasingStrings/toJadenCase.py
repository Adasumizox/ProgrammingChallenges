def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())