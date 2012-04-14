from sys import stdin
from re import match, sub

cpp_pat = r'^[a-z]+(_[a-z][a-z]*)*$'
java_pat = r'^[a-z]+([A-Z][a-z]*)*$'
cpp_extract = r'(_[a-z])[a-z]*?'
java_extract= r'([A-Z])[a-z]*?'
for line in stdin:
    line = line[:-1]
    if match(cpp_pat, line):
        print sub(cpp_extract, lambda m: m.group(1)[1].upper(), line)
    elif match(java_pat, line):
        print sub(java_extract, lambda m: '_'+m.group(1).lower(), line)
    else:
        print 'Error!'
