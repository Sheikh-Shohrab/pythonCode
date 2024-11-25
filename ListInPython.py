myList = [10,20,30,40,50,60]
print(myList)

for i in myList:
    print(i,end=" ")
print("\n")

for i in range(len(myList)):
    print("list[{}] = {}".format( i, myList[i]))