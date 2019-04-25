def to_int_temp(lijn):
    int_lijn = []
    lijn = lijn.split()

    for t in lijn:
        int_lijn.append(int(t))
    return int_lijn

lijnen = []

with open('temperaturen.txt') as bestand:
    lijnen = bestand.readlines()

aantal_25_plus = 0
aantal_30_plus = 0
hittegolven = []

for lijn in lijnen:

    temp = to_int_temp(lijn)

    for i in range(len(temp)):

        if temp[i] >= 30:
            aantal_30_plus += 1

        if temp[i] >= 25:
            aantal_25_plus += 1
        else:
            if aantal_25_plus >= 5 and aantal_30_plus >= 3:
                hittegolven.append((i - aantal_25_plus, i))

            aantal_25_plus = 0
            aantal_30_plus = 0




# print(i, len(temp))
#
# print(aantal_30_plus)
# print(aantal_25_plus)
# print(hittegolven)