#Kleine letters worden hoofdletters;
#Elk teken wordt vervangen door een teken dat n plaatsen (n<32) verder staat in de ASCII-tabel;
#Indien het nieuwe teken een apenstaartje is, vervang dan het apenstaartje door een spatie;
#Een spatie tussen twee woorden in de leesbare tekst wordt in de versleutelde tekst vervangen door een apenstaartje.

#def versleutel_woord(woord, n):
#    nieuw_woord = ''
#    uitkomst = ''
#    for letter in woord:
#        nieuw_woord += letter.upper()
#    for letter in nieuw_woord:
#        if chr(ord(letter) +n) == '@':
#            uitkomst += ' '
#        elif chr(ord(letter) +n) == ' ':
#            uitkomst += '@'
#        else:
#            uitkomst += chr(ord(letter) +n)
#    return uitkomst

#def versleutel_zin(zin, n):
#    nieuwe_zin = ''
#    for letter in zin:
#        if letter == ' ':
#            nieuwe_zin += '@'
#        else:
#            nieuwe_zin += versleutel_woord(letter, n)
#    return nieuwe_zin

def versleutelde_woorden(woord, n):
    versleuteld_woord = ''
    woord = woord.upper()
    for letter in woord:
        versleutelde_letter = chr(ord(letter) + n)
        if versleutelde_letter == '@':
            versleutelde_letter = ' '
        versleuteld_woord += versleutelde_letter

    return versleuteld_woord

print(versleutelde_woorden('?kaas?', 1))