import sys
import re
for s in sys.stdin.read().splitlines():
    operation, _type, name = s.split(';')
    if operation == 'C':
        if _type == 'C':
            combine_class = name.split()
            print(''.join([i.capitalize() for i in combine_class]))
        else:
            temp_hold = name.split()
            combine_other = [i.capitalize() for i in temp_hold[1:]]
            combine_other.insert(0,temp_hold[0])
            print(''.join(combine_other) + ('()' if _type == 'M' else ''))
    if operation == 'S':
        if _type == 'C':
            split_class = re.findall('[A-Z][^A-Z]*', name)
            print(' '.join([i.lower() for i in split_class]))
        else:
            split_other = re.findall('[a-zA-Z][^A-Z]*', name.split('()')[0])
            print(' '.join([i.lower() for i in split_other]))

