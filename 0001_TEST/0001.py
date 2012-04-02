import sys

for line in sys.stdin:
    print line[:-1] if eval(line, {}, {}) is not 42 else exit(0)
