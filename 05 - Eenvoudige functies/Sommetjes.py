# invoer
a = float(input('geef a ∈ ]0,20[: '))
b = float(input('geef b ∈ ]0,20[: '))

# bewerking

resultaat1 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(a, b,(a + b))
resultaat2 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10), (b * 10),((a * 10) + (b * 10)))
resultaat3 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10 ** 2), (b * 10 ** 2),((a * 10 ** 2) + (b * 10 ** 2)))
resultaat4 =  '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10 ** 3), (b * 10 ** 3),((a * 10 ** 3) + (b * 10 ** 3)))
resultaat5 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((a * 10 ** 4), (b * 10 ** 4),((a * 10 ** 4) + (b * 10 ** 4)))

# uitvoer

print(resultaat1)
print(resultaat2)
print(resultaat3)
print(resultaat4)
print(resultaat5)
