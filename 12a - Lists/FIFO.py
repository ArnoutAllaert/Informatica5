invoer = input('invoer: ')
qeue = []
while invoer != 'STOP':
    if invoer != '?':
        qeue.append(invoer)

    elif len(qeue) > 0:
        print(qeue.pop(0))

    invoer = input('invoer: ')
