def ontdubbelen(woord):
    nieuw_woord = woord
    uitkomst = nieuw_woord
    for i in range(0, len(woord) - 1):
        if woord[i] == woord[i + 1]:
            nieuw_woord = woord[:i] + woord[i + 1:]
    for i in range(0, len(nieuw_woord) - 1):
        if nieuw_woord[i] == nieuw_woord[i + 1]:
           uitkomst = nieuw_woord[:i] + nieuw_woord[i + 1:]


    return uitkomst

print(ontdubbelen('aaien'))
print(ontdubbelen('stress'))
print(ontdubbelen('grootte'))
print(ontdubbelen('eieren'))

