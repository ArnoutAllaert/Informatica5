def ontdubbelen(woord):
    for i in range(0, len(woord) - 1):
        if woord[i] == woord[i + 1]:
            woord = woord[:i] + woord[i + 1]

    return woord

print(ontdubbelen('stress'))