def variableLenthArgu(arg, *var):
    print(arg)
    print(id(arg))
    print(id(var))
    for i in var:
        print(i)
    return
variableLenthArgu(10)
variableLenthArgu(20,30,40,50)


def sum(*arg):
    result = 0
    for x in arg:
       result = result + x 
    return result
print(sum(10,20,30,40,50))
