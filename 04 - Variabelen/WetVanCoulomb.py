# invoer
q1 = 2.0E-6
q2 = 1.0E-6
k = 8.99E9
r = float(input('Geef r: '))

# bereking
resultaat = k * ((q1 * q2) / (r *10 ** -2) **2)

# uitvoer
print(resultaat)