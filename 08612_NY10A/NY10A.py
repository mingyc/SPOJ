seq_len = 40
patterns = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']

P = input()
for p in xrange(P):
    print raw_input(),
    seq = raw_input().strip()
    occurence = dict.fromkeys(patterns, 0)
    for i in xrange(seq_len-2):
        occurence[seq[i:i+3]] += 1 
    print ' '.join(str(occurence[p]) for p in patterns)
