def callByValue(var):
    var = var+1
    print("inside funtion: ",id(var))

var = 10
print ("previous: ",id(var))
callByValue(var)

def callByRefChcek(arg):
    arg = arg.append(100)
    print("From function: ",arg)
    print(id(arg))

myList = [10,20,30,40]
print("List: ",myList)
print("Lis ID: ",id(myList))
callByRefChcek(myList)
