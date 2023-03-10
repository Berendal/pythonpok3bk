# regex = r'\b(\w+)\s+\1\b'
# regex = r'\d{2}((-|---|\.)?)(\d{2}\1){2}\d{2}'
# regex = r'\d{2}(-?)(\d{2}\1){2}\d{2}'
# regex = r'\b\w*(\w)\w*\1{1,}\w*\b'
# regex = r'(.)(.)(.)(.).\4\3\2\1'
# regex = r'(ok){3,}'
# regex = r'([a-z])([0-9]|\w)([A-Z])\1\2\3'
# regex = r'((bee)(geek){1,}){1,}'
# regex = r'(\([2-9]\d{2}\)|[2-9]\d{2})[\s-][2-9]\d{2}-\d{4}'
# regex = r'\d{5}(-\d{4})?'

# regex = r'^[0-9]{1,2}[a-zA-Z]{3,}\.{,3}$'
# regex = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'
# regex = r'^[a-zA-Z02468]{40}[13579\s]{5}'
# regex = r'^[a-z|A-Z]*s$'
# regex = r'^\d{2,}[a-z]*[A-Z]*$'
# regex = r'.*?\(.+\).*' | regex = r'.*\(.*\).*'
# regex = r'\b[A-Z]\w*\b'
# regex = r'\b[A-Z]+\b'
# regex = r'\b[aA][n]?\b'


# import re 
# for line in 'Some words contain the word cat: scat, ducati, alcatel, catalyst, worldcat and of course cat!'.split(): 
#     if re.search(r"\Bcat\B", line, flags=0): 
#         print(line, sep='\n')


# regex = r'ca[rtb]'
# regex = r'[0-9|[A-F]'
# regex = r'[A-Za-z]\d{4}'
# regex = r'[a-z]\d[a-z][A-Z]{2}'
# regex = r'\d[aeiouy][^bcDF]\S[^AEIOUY][^,.]'
# regex = r'[1-3][0-2][12x][03aA][xsu][.,]'
# regex = r'(\S7\d{10}|\S7.\d{3}.\d{7}|\S7.\d{3}.-\d{3}-\d{2}-\d{2}|\S7\s\d{3}\s\d{3}\s\d{2}\s\d{2})'
# regex = r'\d{2}\.\d{2}\.\d{4}|\d{2}\/\d{2}\/\d{4}|\d{4}\.\d{2}\.\d{2}|\d{4}\/\d{2}\/\d{2}'
# regex = r'([0-1][0-9]|[0-3]{2}):[0-5][0-9]'
# regex = r'[A-Z]{5}\d{4}[A-Z]'
# regex = r'[A-Z]{1,2}\d(\d|[A-Z])?\s\d[ABD-HJLNP-UW-Z]{2}'

# import re


# a = [r'7-\d{3}-\d{3}-\d{2}-\d{2}', r'8-\d{3}-\d{4}-\d{4}']

# print(*re.findall(r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}', r'Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911'))