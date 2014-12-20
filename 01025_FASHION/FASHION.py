from sys import stdin

t = int(stdin.next())
for i in xrange(t):
    N = int(stdin.next())
    h1 = sorted(map(int, stdin.next().split()))
    h2 = sorted(map(int, stdin.next().split()))
    print sum(h*h2[j] for j, h in enumerate(h1))
