N = int(raw_input())
for n in xrange(N):
    M, word = raw_input().split()
    M = int(M)
    print n+1, word[:M-1] + word[M:]
