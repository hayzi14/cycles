n = int(input(" число = "))

a = 0
b = 1

while n > 0:
    d = n % 10
    a = a + d
    b = b * d
    n = n // 10

print("сумма:", a)
print("произведение:", b)