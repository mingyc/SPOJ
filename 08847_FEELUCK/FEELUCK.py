from collections import defaultdict
import re

for case in range(input()):
    URLs = defaultdict(list)
    for count in range(10):
        url, relevance = re.split(r'(\S{1,100})\s*(\d+)', raw_input())[1:3]
        URLs[int(relevance)].append(url)
    print 'Case #{0}:\n{1}'.format(case+1, '\n'.join(URLs[sorted(URLs)[-1]]))
