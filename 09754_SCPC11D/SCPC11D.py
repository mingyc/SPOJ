for line in iter(raw_input, '0 0 0'):
    a, b, c = sorted(map(int, line.split()))
    print 'right' if (c**2 == a**2 + b**2) else 'wrong'
