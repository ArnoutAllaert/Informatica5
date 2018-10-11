hendel_trekken = str(input('trek aan de hendel van de wissel (ja/nee) '))
man_duwen = input('man van brug duwen ')

if hendel_trekken == 'ja':
    if man_duwen == 'ja':
        doden = 2

    else:
        doden = 1

if hendel_trekken == 'nee':
    if man_duwen == 'ja':
        doden = 1

    else:
        doden = 5

print(str(doden))
