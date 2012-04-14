import math

moduler = 1298074214633706835075030044377087
max_n = 500
sum_of_exp = [1] + [None]*max_n
for i in xrange(1, max_n+1):
    sum_of_exp[i] = sum_of_exp[i-1]*2+1
    if sum_of_exp[i] > moduler:
        sum_of_exp[i] %= moduler

T = int(raw_input())
for t in xrange(T):
    print sum_of_exp[int(raw_input())]
