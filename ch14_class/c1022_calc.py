class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    # sub
    def sub(self, num):
        self.result -= num
        return self.result
    # mul
    def mul(self, num):
        self.result *= num
        return self.result

    # div
    def div(self, num):
        self.result /= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(2))
print(cal2.add(5))