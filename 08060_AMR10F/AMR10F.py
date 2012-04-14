T = int(raw_input())
for t in xrange(T):
    N, A, D = [int(num) for num in raw_input().split()]
    print (A*2 + D*N - D) * N / 2  # trapezoidal rule
