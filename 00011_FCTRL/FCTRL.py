from sys import stdin

stdin.next()
for N in map(int, stdin):
    zeroes, five = 0, 5
    while five <= N:
        zeroes += N/five
        five *= 5
    print zeroes
