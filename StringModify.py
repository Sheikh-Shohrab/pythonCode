import array as ar
var = "WORD"
print(var)

stringToList = list(var)    #convert string to list.
print("Previous modifying: ",var)
print(id(var))
print(stringToList)
print(id(stringToList))
stringToList.insert(3, 'L')
print(stringToList)
print(id(stringToList))

var = ''.join(stringToList)
print("After modifying: ",var)
print(id(var))

var = 10
print(var)
print(id(var))

var = 20
print(var)
print(id(var))

myString = "WORD"
print(myString)
msModify = ar.array('u', myString)  #convert unicode string to array
msModify.insert(3, "L")
myString = msModify.tounicode()
print(myString.title()) #title means first world is capital.