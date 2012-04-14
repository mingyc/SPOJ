T = int(raw_input())
for t in xrange(T):
    turns = 0
    N = int(raw_input())
    for i, S in enumerate(raw_input().split()):
        turns += int(S) / (i+1)
    print ('BOB', 'ALICE')[turns % 2]
