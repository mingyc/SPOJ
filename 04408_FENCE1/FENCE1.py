from math import pi

L = int(raw_input())
while L is not 0:
    print '%0.2f' % (L**2/(2*pi),)
    L = int(raw_input())
