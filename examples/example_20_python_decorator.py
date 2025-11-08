# Python: simple decorator + generator example
def deco(fn):
    def wrapper(*a, **k):
        print("Running decorated function")
        return fn(*a, **k)
    return wrapper

@deco
def fib(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b

print(list(fib(10)))
