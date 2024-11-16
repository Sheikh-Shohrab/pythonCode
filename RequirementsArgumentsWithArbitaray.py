def myTester(firstTest, *exceptTest):
    maxExcept = max(exceptTest)
    result = (firstTest + maxExcept)/2

    return result

print(myTester(8, 9, 7, 5, 4))