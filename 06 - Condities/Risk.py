# invoer
a1 = int(input('aantal ogen dobbelsteen: '))
a2 = int(input('aantal ogen dobbelsteen: '))
a3 = int(input('aantal ogen dobbelsteen: '))
v1 = int(input('aantal ogen dobbelsteen: '))
v2 = int(input('aantal ogen dobbelsteen: '))

#sorteren
sa1 = max(a1, a2, a3)
sa2 = a1 + a2 + a3 - sa1 - min(a1, a2, a3)

sv1 = max(v1, v2)
sv2 = min(v1, v2)

#winnaar bepalen
if sa1 > sa2 and sa2 > sv2:
    mes = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif sv2 >= sa1 and sv2 >= sa2:
    mes = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'
else:
    mes = 'aanvaller verliest 1eger, verdediger verliest 1eger'

#uitvoer
print(mes)