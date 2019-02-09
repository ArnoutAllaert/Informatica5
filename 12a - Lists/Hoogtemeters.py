def hoogtemeters(hoogtes):
    a = 1
    mes = []
    while a < len(hoogtes):
        mes.append(hoogtes[a] - hoogtes[a - 1])
        a += 1
    return mes

def dalen_en_stijgen(hoogtes):
    x = 0
    y = 0
    for hoogte in hoogtes:
        if hoogte < 0:
            x -= hoogte
        else:
            y += hoogte
    return x, y

print(hoogtemeters([22, 22]))
print(hoogtemeters([822, 61, 347, 234, 883, 336]))
print(dalen_en_stijgen([0]))
#(0, 0)
print(dalen_en_stijgen([-761, 286, -113, 649, -547]))
#(1421, 935)