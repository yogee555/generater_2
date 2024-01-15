def xyz():
    print("hi")
    print("do")
    yield 10
    print("to")
    print("ooo")
    yield "execute finished"
a = xyz()
print(a.__next__())

if a.__next__() == "execute finished":
    print("success")