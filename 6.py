n = int(input('Положительное число = '))
a = [] 
if n < 0 :
         print ('error')
else:
        while n != 0:
            a.append(n % 10)
            n = n // 10
a.reverse()
print(a)