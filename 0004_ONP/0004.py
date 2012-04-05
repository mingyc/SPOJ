from sys import stdin

def postfix(infix):
    op_priority = { '(': 0, '+': 1, '-': 2, '*': 3, '/': 4, '^': 5 }
    stack = []
    for ch in infix:
        if ch =='(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                yield stack.pop()
            stack.pop()
        elif ch in op_priority:
            while op_priority[stack[-1]] >= op_priority[ch]:
                yield stack.pop()
            stack.append(ch)
        else:
            yield ch

        
stdin.readline()
for expr in stdin:
    print ''.join(postfix(expr[:-1]))
