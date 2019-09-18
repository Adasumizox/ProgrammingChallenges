def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

# We can also use insecure version.
#def basic_op(operator, value1, value2):
#    return eval("{}{}{}".format(value1, operator, value2))