# Function to add two numbers
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Class to perform basic arithmetic operations
class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b