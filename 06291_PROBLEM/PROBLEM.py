N = int(raw_input())
for n in xrange(N):
    print sum([{"0": 1, "6": 1, "8": 2, "9": 1}.get(c, 0) for c in raw_input()])
