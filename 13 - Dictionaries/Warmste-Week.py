def gift_inschrijven(klas, giften):
    if klas[0] in giften:
        giften[klas[0]] += klas[1]
    else:
        giften[klas[0]] = klas[1]
    return giften