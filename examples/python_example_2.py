
"""
Program 3: OOP Class Example
"""
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} makes a sound"

print(Animal("Dog").speak())

