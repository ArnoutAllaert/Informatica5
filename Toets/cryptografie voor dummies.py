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

def versleutel_woord(woord, n):
    code = ''
    woord = woord.upper()
    for letter in woord:
        code_letter = chr(ord(letter) + n)

        if code_letter == '@':
            code_letter = ' '
        code += code_letter

    return code

def versleutel_zin(zin, n):
    index_spatie = zin.find(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie + 1:]

        code += '@' + versleutel_woord(woord, n)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel_woord(zin, n)

    return code


print(versleutel_zin('er is niemand thuis zzz 9810.', 1))
