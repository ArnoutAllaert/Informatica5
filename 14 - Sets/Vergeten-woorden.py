def vergeten_woorden(tekst, verplicht):
    gebruikt = 0
    vergeten = 0
    lijst = tekst.split()
    kaas = set(lijst)
    woorden = kaas.intersection(verplicht)

    return len(verplicht), len(verplicht) - len(woorden), len(woorden)






print(vergeten_woorden('hello world world world', {'python', 'world', 'hello', 'java'}))
#(4, 2, 2)