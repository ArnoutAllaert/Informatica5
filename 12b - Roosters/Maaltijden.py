def dagprijs(tuple):
    prijs = 0
    for i in range(0, len(tuple), 2):
        if tuple[i] == 'middagmaal':
            prijs += tuple[i + 1] * 5.3
        elif tuple[i] == 'soep':
            prijs += tuple[i +1] * 1.7
        elif tuple[i] == 'vieruurtje':
            prijs += tuple[i + 1] * 2.3
    return prijs

def weekprijs(tuple):
    prijs = 0
    for dag in tuple:
        prijs += dagprijs(dag)
    return prijs

print( dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2)))
print(dagprijs(('middagmaal', 2, 'vieruurtje', 2)))
print( weekprijs((('middagmaal', 2, 'soep', 2, 'vieruurtje', 2), ('middagmaal', 1, 'soep', 1), ('soep', 3, 'vieruurtje', 3), ('middagmaal', 3, 'soep', 1), ('middagmaal', 3, 'soep', 3, 'vieruurtje', 1))))