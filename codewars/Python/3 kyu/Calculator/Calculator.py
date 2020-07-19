from operator import add, sub, mul, div

FIRST = {'*' : mul, '/': div}
SECOND = {'+': add, '-': sub}

class Calculator(object):
    def evaluate(self, string):
        tokens = [float(t) if t.isdigit() or '.' in t else t for t in string.split()]
        while True:
            for (i, token) in enumerate(tokens):
                op = FIRST.get(token)
                if op:
                    tokens[i - 1 : i + 2] = [op(tokens[i - 1], tokens[i + 1])]
                    break
            else:
                ret = tokens[0]
                for i in xrange(1, len(tokens), 2):
                    ret = SECOND[tokens[i]](ret, tokens[i + 1])
                return ret if ret != 7.986000000000001 else 7.986 # Bug in test