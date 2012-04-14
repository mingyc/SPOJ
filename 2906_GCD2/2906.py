from sys import stdin, stdout

def gcd(a, b):
    return a if not b else gcd(b, a%b)

stdin.readline()
for line in stdin:
    A, B = line.split()
    stdout.write(str(gcd(int(A), int(B))) + "\n")
