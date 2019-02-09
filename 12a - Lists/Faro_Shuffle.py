def nieuw_kaartspel(kleuren, cijfers):
    kaartspel = []
    a = 0
    b = 0
    while a < len(kleuren):
        while b < len(cijfers):
            kaartspel.append(kleuren[a] + cijfers[b])
            b += 1
        a += 1
        b = 0
    return kaartspel


def splits_kaartspel(list):
    return (list[0: len(list) // 2], list[len(list) // 2:])

def faro_shuffle(k1, k2):
    shuffle = []
    a = 0
    if len(k1) == len(k2):
        while a < len(k1):
            shuffle.append(k1[a])
            shuffle.append(k2[a])
            a += 1
    else:
        while a < len(k1):
            shuffle.append(k1[a])
            shuffle.append(k2[a])
            a += 1
        shuffle.append(k2[a])
    return shuffle

print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1']))
#['dood 0', 'liefde 1', 'dood 1', 'tijd 0', 'liefde 0', 'tijd 1']
print(faro_shuffle(['blad 1', 'blad 2', 'blad 3', 'steen 1'],['steen 2', 'steen 3', 'schaar 1', 'schaar 2', 'schaar 3']))
#['blad 1', 'steen 2', 'blad 2', 'steen 3', 'blad 3', 'schaar 1', 'steen 1', 'schaar 2', 'schaar 3']
print(faro_shuffle([],['James 7']))
#['James 7']