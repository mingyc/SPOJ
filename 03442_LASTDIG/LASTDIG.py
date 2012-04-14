def modular_pow(base, exp, modulus=10):
    result = 1
    while exp > 0:
        if (exp & 1) == 1:
            result = (result * base) % modulus
        exp >>= 1
        base = (base * base) % modulus
    return result

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        print modular_pow(*map(int, raw_input().split()))
