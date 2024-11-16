def subjectMarksAcceptor(math, sci, **optional):
    print("Match: ",math)
    print("Science: ",sci)
    s = math+sci
    for k,v in optional.items():
        print("{}: {}".format(k,v))
        s = s+v
    return (s/len(optional)+2)

avg_number = subjectMarksAcceptor(math=70, sci=80, bangla = 50, english = 70, algorithm = 90)
print("Your average marks = ",avg_number)