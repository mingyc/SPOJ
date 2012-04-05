T = int(raw_input())
for t in xrange(T):
    print reduce(lambda x, y: x*y, range(1, int(raw_input())+1))
