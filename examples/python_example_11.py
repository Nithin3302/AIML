
"""
Program 2: Decorators
"""
def debug(fn):
    def wrapper(*a, **k):
        print("Calling", fn.__name__)
        return fn(*a, **k)
    return wrapper

@debug
def greet(name):
    print("Hello", name)

greet("Python")

