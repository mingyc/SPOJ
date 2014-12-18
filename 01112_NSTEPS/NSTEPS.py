from sys import stdin

stdin.next()
for line in stdin:
    x, y = map(int, line.split())
    if x == y:
        print x*2 - 1*(x%2)
    elif y == x-2:
        print x+y - 1*(x%2)
    else:
        print 'No Number'
