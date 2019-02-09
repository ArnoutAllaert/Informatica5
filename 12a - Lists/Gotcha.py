def ik_heb_gemoord(list, naam):
    if len(list) == 1:
        x = list[0]
    elif list.index(naam) + 1 >= len(list):
        x = list[1]
        list.pop(0)
    elif list.index(naam) + 2 >= len(list):
        x = list[0]
        list.pop(list.index(naam)+1)
    else:
        x = list[list.index(naam)+2]
        list.pop(list.index(naam)+1)
    return (x, list)

def ik_ben_vermoord(list, naam):
    if len(list) == 1:
        x = list[0]
    elif list.index(naam) + 1 >= len(list):
        x = list[0]
        list.pop(list.index(naam))
    else:
        x = list[list.index(naam)+ 1]
        list.pop(list.index(naam))
    return (x, list)

print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))
#('jan', ['jan', 'piet'])
print(ik_ben_vermoord(['jan'],'jan'))
#('jan', ['jan'])
print(ik_ben_vermoord(['jan', 'joris', 'korneel'],'jan'))