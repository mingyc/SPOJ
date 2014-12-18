from sys import stdin

for a1, a2, a3 in map(lambda l: map(int, l.split()), stdin):
    if a1 == a2 and a2 == a3 and a3 == 0:
        break

    if a2*a2 == a1*a3:
        print 'GP', a3*(a3/a2)
    else:
        print 'AP', a3+a3-a2
