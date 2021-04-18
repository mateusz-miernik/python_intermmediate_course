class Number:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        other = other.number
        new_num = self.number + other
        return Number(new_num).number

    def __iadd__(self, other):
        other = other.number
        new_num = self.number + other
        return Number(new_num)


num1 = Number(2)
num2 = Number(4)
num3 = num1+num2
num1 += num2
print(num3)
print(num1.number)

a = 4
b = 3
b += a
print(b)

Exception()