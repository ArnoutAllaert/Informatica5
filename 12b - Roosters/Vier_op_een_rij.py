def printbaar_rek(lijst):
    mes = ''
    lijst.reverse()
    for i in lijst:
        if lijst.index(i) == len(lijst) -1:
            mes += ''.join(i)
        else:
            mes += ''.join(i) + '\n'
    return mes

def speel(kleur, nummer, rek):
    i = 0
    while i < len(rek):
        if rek[i][nummer] == 'O':
            rek[i].insert(nummer, kleur)
            rek[i][nummer + 1: nummer + 2] = []
            i = len(rek)
        else:
            i += 1
    return rek

print( speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))