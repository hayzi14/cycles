a = int(input(' число = '))
b = int(input(' степень = '))
t = 1

if b > 0:
        for i in range(b+1):
            if i == 0:
                continue
            t*=a
        print(t)