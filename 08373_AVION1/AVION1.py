from sys import stdin

rows = ' '.join(str(i+1) for i, code in enumerate(stdin.readlines()) if code.find('FBI') >= 0)
print rows if len(rows) else 'HE GOT AWAY!'
