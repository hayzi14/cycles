n = int(input(' N = '))

a = [0, 1]

for i in range(n+1):
    if n <= 1:
            break
    elif i == 0:
            continue

    a.append(a[i-1]+a[i])

if n > 1:
    a.pop(-1)

print(a)