from sys import stdin

DUCKY = 'Ducky'
stdin.readline()
for line in stdin:
    count = 0
    for ch in line:
        if ch == '.':
            continue
        elif ch in DUCKY:
            count += 1
            if count == 5:
                print 'DUCKY IS HERE!'
                break
        else:
            print 'NO DUCKY!'
            break
