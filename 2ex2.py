
name = "lzl"
def f1():
    name = "Eric"
    def f2():
        global name
        name = "Snor"  
    f2()
f1()
print(name)






name = "lzl"
def f1():
    name = "Eric"
    def f2():
        global name
        print(name)
    f2()
f1()
