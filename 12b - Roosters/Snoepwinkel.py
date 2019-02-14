def bereken_prijs(list):
    prijs = 0
    for i in list:
        prijs += i[1]
    return prijs

def winkelbriefje(list):
    ticket = []
    for i in list:
        ticket.append(i[0])
    return ticket

def sorteer(list):
    from operator import itemgetter
    list.sort(key=itemgetter(1))
    return list

print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
print(sorteer([('Crocky Zout', 1.39)]))