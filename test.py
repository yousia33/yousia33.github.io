def dec(func):
    def wrapper(*args, **kwargs):
        print('decorate')
        res=func(*args, **kwargs)
        return res
        
    return wrapper

@dec
def test(x):
    print('hahha'+str(x))
    return x

test(56)