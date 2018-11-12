#invoer
x = int(input('getal: '))

#bewerking
if x == 0:
    uitkomst = 0
elif x == 1 or x == 2:
    uitkomst = 1
elif x > 2:
    def fib(n):
        a,b = 1,1
        for _ in range(n-1):
            a,b = b,a+b
        return a
    uitkomst=(fib(x))

#uivoer
print(uitkomst)