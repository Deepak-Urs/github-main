def russianDoll(doll):
    if doll == 0:
        return
    print('Opening', doll, 'th doll-')
    russianDoll(doll-1)

russianDoll(10)