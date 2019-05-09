kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}

def bestaat_weg(stad1, stad2, kaart):
    return stad2 in kaart[stad1]

def geen_dubbelburen(stad1, stad2, kaart):
    x = kaart[stad1]
    y = kaart[stad2]
    verschil_x_y = x.difference(y)
    verschil_y_x = y.difference(x)
    if stad2 in verschil_x_y:
        verschil_x_y.remove(stad2)
    if stad1 in verschil_y_x:
        verschil_y_x.remove(stad1)
    return verschil_y_x.union(verschil_x_y)

def bereikbaarheid_meest_afgelegen_stad(kaart):
    aantal_verbindingen = len(kaart)
    for value in kaart.values():
        if len(value) < aantal_verbindingen:
            aantal_verbindingen = len(value)
    return aantal_verbindingen

def bestaat_route(route, kaart):
    i = 0
    while i < (len(route) - 1):
        if route[i+1] in kaart[route[i]]:
            i += 1
        else:
            i += len(route)
    return i < len(route)

print(geen_dubbelburen('Brussel', 'Hasselt', kaart))
#{'Antwerpen'}
print(geen_dubbelburen('Antwerpen', 'Kortrijk', kaart))
#{'Brussel', 'Brugge'}

print(bestaat_route(['Hasselt', 'Brussel', 'Antwerpen', 'Brugge', 'Gent', 'Kortrijk'], kaart))
#True
print(bestaat_route(['Brugge', 'Hasselt', 'Brussel'], kaart))
#False