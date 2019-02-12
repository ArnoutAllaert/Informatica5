def fruitstuk_toevoegen(list, fruit):
    for i in range(0, len(list)):
        if len(fruit) == len(list[i]):
            list[i] = fruit

        elif i + 1 < len(list) and len(list[i]) < len(fruit) and len(list[i + 1]) > len(fruit):
            list.insert(i +1, fruit)
    if len(list[0]) > len(fruit):
            list.insert(0, fruit)
    elif len(list[len(list) -1]) < len(fruit):
        list.append(fruit)
    return list

def maak_fruitmand(list):
    mand = [list[0]]
    for fruit in list:
        fruitstuk_toevoegen(mand, fruit)
    return mand

print(maak_fruitmand(['kiwi', 'peer', 'kiwi', 'peer', 'kiwi']))
#['kiwi']
print(maak_fruitmand(['bes', 'appel', 'framboos']))
#['bes', 'appel', 'framboos']

