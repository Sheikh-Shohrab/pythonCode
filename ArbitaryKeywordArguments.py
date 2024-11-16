def address(**kwarg):
    for k,v in kwarg.items():
        print("{} : {}".format(k,v))
    return

address(Name = "Shohrab", City = "Dhaka")
address(Name = "Hossain", ID = 2025402003, Email = "cseshorab.cu@gmail.com", Department="CSE")