def boot_overlappend(nieuw, geplaatst):
    overlappend = 0
    for i in nieuw:
        if i in geplaatst:
            overlappend += 1
    return overlappend != 0

def boot_toevoegen(boot, zee):
    kaas = []
    for i in boot:
        kaas += [i]
    if boot_overlappend(boot, zee) == False:
        zee.update(kaas)
    return zee

def vuur(schot, zee):
    kaas = False
    if schot in zee:
        zee.remove(schot)
        kaas = True
    return kaas, zee
