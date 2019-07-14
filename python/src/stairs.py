def stairs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    for i in range(n):
        total += stairs(n-i-2)
    return total + 1

print(stairs(3))
print(stairs(4))
print(stairs(5))
