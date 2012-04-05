N = int(raw_input())
while N != -1:
    packets = []
    for n in xrange(N):
        packets.append(int(raw_input()))
    total = sum(packets)
    avg = total / N
    if total % N == 0:
        print sum([n-avg for n in packets if n > avg])
    else:
        print -1
    N = int(raw_input())
