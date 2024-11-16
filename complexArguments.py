def myFunction(x, z,/,a , *, y):
    print(x,y,z,a)
    sum = x + y+ z+a
    return sum

print(myFunction(50, 40, 70, y = 10))