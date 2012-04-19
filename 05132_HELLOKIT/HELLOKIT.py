for line in iter(raw_input, '.'):
    W, n = line.split()
    pattern, W_len = W*int(n), len(W)
    print '\n'.join([pattern[i:]+pattern[0:i] for i in xrange(W_len)])
