def myFunction(x,/, z, *, y):
    sum = x + y+ z
    return sum

print(myFunction(10, 10, y = 10))