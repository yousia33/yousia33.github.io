def foo(x):
    def go(y):
        nonlocal x 
        x=x+y
        return x
    return go

a=foo(100)
print(a)
