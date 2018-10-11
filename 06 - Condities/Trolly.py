hendel_trekken = str(input('trek aan de hendel van de wissel (ja/nee) '))
dikzak = input('man van brug duwen ')

if hendel_trekken == 'ja':
    if dikzak == 'ja':
        print('2')

    else:
        print('1')

if hendel_trekken == 'nee':
    if dikzak == 'ja':
        print('1')

    else:
        print('5')
