
name = "lzl"
def f1():
    name = "Eric"
    def f2():
        nonlocal name
        name = "Snor"
        print(name)
    f2()
f1()

name = "lzl"
def f1():
    name = "Eric"
    def f2():
    	global name
    	name = "Snor"
    f2()
    print(name)
f1()
