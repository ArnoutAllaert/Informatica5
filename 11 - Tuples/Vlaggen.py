def vlag(richting, kleuren):
    mes = ''
    for i in range(0, len(kleuren)):
        if richting == 'verticaal':
            if i < len(kleuren) -1:
                mes += kleuren[i] + ' | '
            else:
                mes += kleuren[i]
        if richting == 'horizontaal':
            if i < len(kleuren) - 1:
                mes += kleuren[i] + '\n-\n'
            else:
                mes += kleuren[i]
    return mes

print(vlag('verticaal',('zwart', 'geel', 'rood')))
print(vlag('horizontaal',('rood', 'wit', 'blauw')))