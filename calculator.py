from math import nan



class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        return(self.op1 + self.op2)

    def subtract(self):
        return(self.op1 - self.op2)

    def multiply(self):
        return(self.op1 * self.op2)

    def divide(self):
        if self.op2 == 0:
            return nan
        return (self.op1 / self.op2)
"""
Przykłady wywołania kalkulatora:
"""
if __name__ == "__main__":  # pragma: no cover

    print(Calculator(10.0, 2.0).sum())  # 12.0
    print(Calculator(10.0, 2.0).subtract()) # 8.0
    print(Calculator(10.0, 2.0).multiply()) # 20.0
    print(Calculator(10.0, 2.0).divide()) # 5.0
    print(Calculator(10.0, 0.0).divide()) # nan
