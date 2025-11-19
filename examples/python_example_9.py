
"""
Program 10: Basic class with methods
"""
class Counter:
    def __init__(self):
        self.v=0
    def inc(self):
        self.v+=1
    def value(self):
        return self.v

c=Counter()
for _ in range(5):
    c.inc()
print(c.value())

