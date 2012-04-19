import re
n_len = 6

def nAmB(n1, n2, A, B):
    if sum(1 for e in zip(n1, n2) if e[0] == e[1]) != A:
        return False
    mB = 0
    for i in range(n_len):
        for j in range(n_len):
            if i != j and n1[i] == n2[j]:
                mB += 1
    return mB == B

def guess(A=-1, B=-1, _validset=[True]*(10**n_len), _cur=[0], _i2s=lambda i: '{0:0{1}}'.format(i, n_len)):
    if (A, B) == (-1, -1):  # initial
        return _i2s(_cur[0])
    elif (A, B) != (n_len, 0): 
        _validset[_cur[0]], _cur_next = False, _cur[0]
        for i in xrange(len(_validset)):
            if _validset[i] and not nAmB(_i2s(_cur[0]), _i2s(i), A, B):
                _validset[i] = False
            if _cur_next == _cur[0] and _validset[i]:
                _cur_next = i
        _cur[0] = _cur_next
    return _i2s(_cur[0])
    

if __name__ == "__main__":
    print guess()
    A, B = map(int, re.split(r'[A-Ba-b]', raw_input())[:-1])
    while (A, B) != (n_len, 0):
        print guess(A, B)
        A, B = map(int, re.split(r'[A-Ba-b]', raw_input())[:-1])
