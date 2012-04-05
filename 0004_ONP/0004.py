from sys import stdin, stdout

def postfix(infix):
    operators = { '(': 0, '+': 1, '-': 2, '*': 3, '/': 4, '^': 5 }
    stack = []
    for ch in infix:
        if ch =='(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                yield stack.pop()
            stack.pop()
        elif ch in operators:
            while operators[stack[-1]] >= operators[ch]:
                yield stack.pop()
            stack.append(ch)
        else:
            yield ch
        
if __name__ == '__main__':
    stdin.readline()
    map(stdout.write, map(''.join, map(postfix, stdin)))
