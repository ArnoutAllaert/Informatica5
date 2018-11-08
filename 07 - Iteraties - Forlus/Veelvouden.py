#invoer
r = int(input('geef r∈N0 met r<100: '))
som_veelvouden = 0
#bewerking
for i in range(r,101 ,r ):
    som_veelvouden += i

#uitvoer
print(som_veelvouden)
