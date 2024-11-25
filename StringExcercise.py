mystr = "I love my bangladesh, It's so beautiful country"
vowel = "aeiou"
count = 0

for x in mystr:
    if x.lower() in vowel:
        print(x)
        count +=1
print("Total vowels: ",count)