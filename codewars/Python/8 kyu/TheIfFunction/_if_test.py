# HACK workaround to access `_if` in solution module
for k, v in vars(__import__('solution')).items():
    if k == "_if":
        vars()[k] = v
a = False;
b = False;
c = False;
d = False;
e = False;

def a1():
    Test.expect(True)
    global a
    a = True

def a2():
    Test.expect(False, "Should respond to True correctly")

def b1():
    Test.expect(False, "Should support falsy/truesy values")

def b2():
    Test.expect(True)
    global b
    b = True

def c1():
    Test.expect(True)
    global c
    c = True

def c2():
    Test.expect(False, "Should support falsy/truesy values")

def d1():
    Test.expect(True)
    global d
    d = True

def d2():
    Test.expect(False, "Should support comparison")

def e1():
    Test.expect(True)
    global e
    e = True

def e2():
    Test.expect(False, "Should support comparison")

_if(True, a1, a2)
_if(False, b1, b2)
_if(1, c1, c2)
_if((3 < 4), d1, d2)
_if((9 % 3 == 0), e1, e2)

Test.expect(a and b and c and d and e)