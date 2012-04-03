from sys import stdin

stdin.readline()
for line in stdin:
    a, b = line.split()
    print str(eval(a[::-1]) + eval(b[::-1]))[::-1].lstrip('0')

