def faculteit(n):
    if n == 1:
        return 1
    else:
        print('{} * faculteit({})'.format(n, n - 1))
        res = faculteit(n - 1)
        print('{} * {} = {}'.format(n, res, n * res))
        return n * res


def isPalindroom(w):
    if len(w) == 1 or len(w) == 0:
        return True
    else:
        print('{} == {} and isPalindroom({})'.format(w[0], w[-1], w[1:-1]))
        res = isPalindroom(w[1:-1])
        print('{} and {}'.format(w[0] == w[-1], res))
        return w[0] == w[-1] and res

print(isPalindroom('koortsmeetsysteemstrook'))