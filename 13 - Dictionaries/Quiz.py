def verlaat_ploeg(naam, ploeg, ploegen):
    ploegen[ploeg].remove(naam)
    if len(ploegen[ploeg]) == 0:
        ploegen.pop(ploeg)
    return ploegen

def vervoegt_ploeg(naam, ploeg, ploegen):
    if ploeg in ploegen:
        ploegen[ploeg].append(naam)
    else:
        ploegen[ploeg] = [naam]
    return ploegen

print( verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(verlaat_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))