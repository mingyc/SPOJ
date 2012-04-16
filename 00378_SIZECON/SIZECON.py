i=input
print sum(filter(lambda n:n>0, (i() for n in range(int(i())))))
