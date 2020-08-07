
def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decor #Remove line number 11, change resultfun to num and insert @decor
def num():
    return 5

print(num())
