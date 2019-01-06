def is_letter(n):
    if n in 'abcdefghijklmnopqrstuvwxyz' or n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        waarheid = True
    else:
        waarheid = False
    return waarheid


def roteer_letter(n, k):
    def is_letter(n):
        if n in 'abcdefghijklmnopqrstuvwxyz' or n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            waarheid = True
        else:
            waarheid = False
        return waarheid
    if is_letter(n) == True:
        if n in 'abcdefghijklmnopqrstuvwxyz':
            if ord(n) + k > 122:
                return chr((ord(n) + k) - 26)
            else:
                return chr(ord(n) + k)

        elif n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ord(n) + k > 90:
                return chr((ord(n) + k) - 26)
            else:
                return chr(ord(n)+k)

    else:
        return n


def versleutel(z, k):
        def roteer_letter(n, k):
            def is_letter(n):
                if n in 'abcdefghijklmnopqrstuvwxyz' or n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    waarheid = True
                else:
                    waarheid = False
                return waarheid

            if is_letter(n) == True:
                if n in 'abcdefghijklmnopqrstuvwxyz':
                    if ord(n) + k > 122:
                        return chr((ord(n) + k) - 26)
                    else:
                        return chr(ord(n) + k)

                elif n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if ord(n) + k > 90:
                        return chr((ord(n) + k) - 26)
                    else:
                        return chr(ord(n) + k)
            else:
                return n

        zin = ''
        for letter in z:
            zin += roteer_letter(letter, k)
        return zin

print(versleutel('H', 20))
print(versleutel('Het leven bestaat voor 10% uit dingen die gebeuren en voor 90% uit hoe jij daarop reageert.', 20))
print(versleutel('Vertrouw op je kracht en vier het leven!',8))