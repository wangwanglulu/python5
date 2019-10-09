
name = "lzl"
def f1():
    name = "Eric"
    def f2():
        name = "Snor"
        print(name)
    f2()
f1()

name = "lzl"
def f1():
    name = "Eric"
    def f2():
        print(name)
    f2()
f1()
