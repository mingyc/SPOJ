from sys import stdin   

stdin.readline()
for string in stdin:
    P, seqlen, wordlen = 0, 1, -1
    for w in string.split():
        curlen = len(w)
        wordlen, seqlen = curlen, seqlen+1 if curlen == wordlen else 1
        P = seqlen if seqlen > P else P
    print P
