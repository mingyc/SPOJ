from sys import stdin

for line in stdin:
    harmonic, c, i = 0.0, float(line), 0 
    if c < 0.01: 
        break
    while harmonic < c:
        harmonic += 1.0 / (i+2)
        i += 1
    print '{0} card(s)'.format(i)
