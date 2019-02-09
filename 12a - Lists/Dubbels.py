def dubbels(list):
    l = []
    for i in list:
        if list.count(i) > 1 and i not in l:
            l.append(i)
    return l

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))
