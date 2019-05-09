kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}

def bestaat_weg(stad1, stad2, kaart):
    return stad2 in kaart[stad1]

def geen_dubbelburen(stad1, stad2, kaart):
    x = kaart[stad1]
    y = kaart[stad2]
    kaas = y.difference(x)
    plopkoek = x.difference(y)
    if stad1 in plopkoek:
        plopkoek.remove(stad1)
    elif stad2 in plopkoek:
        plopkoek.remove(stad2)
    if stad1 in kaas:
        kaas.remove(stad1)
    elif stad2 in kaas:
        kaas.remove(stad2)
    return kaas.union(plopkoek)

def bereikbaarheid_meest_afgelegen_stad(kaart):
    kaas = len(kaart)
    for value in kaart.values():
        if len(value) < kaas:
            kaas = len(value)
    return kaas

def bestaat_route(route, kaart):
    i = 0
    while i < (len(route) - 1):
        if route[i+1] in kaart[route[i]]:
            i += 1
        else:
            i += len(route)
    return i < len(route)


print(bestaat_route(['Hasselt', 'Brussel', 'Antwerpen', 'Brugge', 'Gent', 'Kortrijk'], kaart))
#True
print(bestaat_route(['Brugge', 'Hasselt', 'Brussel'], kaart))
#False