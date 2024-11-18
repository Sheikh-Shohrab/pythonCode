a = 10
b = 20

def accessor():
    a = 30
    b = 40
    print("Increment global variable value")
    globals()['a'] = globals()['a']+10
    globals()['b'] = globals()['b']+20
    print("Local A : ",a)
    print("Local B : ",b)

    print(id(globals()['a']))
    
    return

print(accessor())
print("Global: ",a)
print("Global: ",b)
print(id(a))