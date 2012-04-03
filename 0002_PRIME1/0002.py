from sys import stdin

INPUT_LIMIT = 1000000000
PRIME_TABLE_LIMIT = int(INPUT_LIMIT**0.5)+1
PRIME_RANGE_LIMIT = 100001

def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    for i in xrange(3, int(limit**0.5), 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((limit-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3, limit, 2) if sieve[i]]
base_primes = sieve_of_eratosthenes(PRIME_TABLE_LIMIT)

if __name__ == '__main__':
    output = ''
    stdin.readline()
    for line in stdin:
        m, n = [eval(num) for num in line.split()] 
        m = 2 if m < 2 else m
        isprime = [True] * PRIME_RANGE_LIMIT
        for p in base_primes:
            start = 2*p if p >= m else (m + ((p-m % p) % p))
            isprime[start-m:(n+1)-m:p] = [False] * ((n-start)/p + 1)
        output += '\n'.join([str(i) for i in xrange(m, n+1) if isprime[i-m]]) + '\n\n'
    print output[:-1]
