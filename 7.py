n = int(input(" число = "))
a = 0

while n > 0:
    if n % 2 == 0:
        a += n % 10
    n //= 10

print(a)