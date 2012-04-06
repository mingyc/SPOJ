from sys import stdin, stdout

def postfix(infix, OPERATORS='(+-*/^'):
    op = dict(zip(OPERATORS, xrange(len(OPERATORS))))
    stack = []
    for c in infix:
        if c =='(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                yield stack.pop()
            stack.pop()
        elif c in op:
            while op[stack[-1]] >= op[c]:
                yield stack.pop()
            stack.append(c)
        else:
            yield c
        
if __name__ == '__main__':
    stdin.readline()
    map(stdout.write, map(''.join, map(postfix, stdin)))
