def beweeg(tuple, richting):
    if richting == '<':
        return tuple[0] - 1, tuple[1]
    elif richting == '>':
        return tuple[0] + 1, tuple[1]
    elif richting == '^':
        return tuple[0], tuple[1] + 1
    elif richting == 'v':
        return tuple[0], tuple[1] - 1

def teruggekeerd(list):
    a = 0
    mes = False
    while a < len(list) -1:
        if list[a] == '<' and list[a + 1] == '>' or list[a] == '>' and list[a + 1] == '<':
            mes = True
        elif list[a] == '^' and list[a + 1] == 'v' or list[a] == 'v' and list[a + 1] == '^':
            mes = True
        a += 1
    return mes

def laatste_levende_positie(list):
    a = 0
    zetten = 0
    coordinaten = (0, 0)
    while a < len(list):
        zetten += 1
        if teruggekeerd(list[a : a + 2]) == True:
            coordinaten = beweeg(coordinaten, list[a])
            a = len(list)
        else:
            coordinaten = beweeg(coordinaten, list[a])
            a += 1
    return zetten, coordinaten[0], coordinaten[1]

print(laatste_levende_positie(['>', '<', '^']))
#(1, 1, 0)
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))
#(6, 0, 0)
print(laatste_levende_positie(['^', 'v']))
#(1, 0, 1)
print(teruggekeerd(['^', 'v']))