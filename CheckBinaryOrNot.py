myStr = "01010"

for x in myStr:
    if x not in "01":
        print("Not Binary")
        break
print("Your binary digit is: ",myStr)

Decimal = int(myStr, 2)
print(Decimal)