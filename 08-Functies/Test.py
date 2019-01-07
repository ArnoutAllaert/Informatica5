def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend = n // 2
    else:
        volgend = (n * 3) + 1
    return volgend


def collatz(n):
    collatz = 1
    while volgend_collatz_getal(n) != 1 and n != 1:
        collatz += 1
        n = volgend_collatz_getal(n)
    if n == 1:
        collatz = 1
    elif volgend_collatz_getal(n) == 1:
        collatz += 1

    return collatz
