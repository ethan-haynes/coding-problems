import math
def divide(dividend, divisor):
    negative = True if math.copysign(1,dividend) != math.copysign(1,divisor) else False
    quotient, temp = 0, 0
    for i in range(int(math.fabs(dividend))):
        temp += 1
        if temp == int(math.fabs(divisor)):
            quotient += -1 if negative else 1
            temp = 0
    return quotient

print(divide(10,3))
print(divide(10,-3))
