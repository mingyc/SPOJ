from sys import stdin

def next_row_of_col(c, cols, limit=200):
    rows, cur = limit/cols, c
    for i in xrange(rows):
        a, b = cur, cur + 2*cols - (2*(c+1)-1)
        if a < limit:
            yield a
        if b < limit:
            yield b
        cur += 2*cols

while True:
    cols = eval(stdin.readline())
    if cols is 0:
        break
    msg = stdin.readline()[:-1]
    limit = len(msg)
    ans = []
    for c in xrange(cols):
        ans.extend([msg[i] for i in next_row_of_col(c, cols, limit)])
    print ''.join(ans)

