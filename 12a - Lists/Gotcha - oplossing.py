def ik_heb_gemoord(lijst, moordenaar):
    #slachtoffer schrappen
    index_moordenaar = lijst.index(moordenaar)
    index_slachtoffer = (index_moordenaar + 1) % len(lijst)

    lijst[index_slachtoffer: index_slachtoffer + 1] = []

    #nieuw doel geven aan de moordenaar
    index_moordenaar = lijst.index(moordenaar)
    index_nieuw_doel = (index_moordenaar + 1) % len(lijst)
    return lijst, lijst[index_nieuw_doel]

#ik_ben_vermoord()  zelf doen

print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))
