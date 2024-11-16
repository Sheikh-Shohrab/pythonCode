def posFun(*, num2, num3, num1):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")

posFun(num2=10, num1 = 20, num3=30) 
print("\nHello", "World", sep="-", end="!!\n\n")