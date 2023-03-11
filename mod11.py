# import sys, re


# data = [line.strip() for line in sys.stdin]
# res = 0
# for i in data:
#     if re.search('(beegeek)', i, re.I):
#         res += 1
# print(res)


# print(bool(re.search('^Здравствуйте|^Доброе утро|^Добрый день|^Добрый вечер', input(), re.I | re.M)))


# data = [line.strip() for line in sys.stdin]
# res = 0
# for i in data:
#     if re.search(r'^(beegeek).*(beegeek)$', i):
#         res += 3
#     elif re.search(r'^(beegeek)', i) or re.search(r'(beegeek)$', i):
#         res += 2
#     elif re.search(r'.*(beegeek).*', i):
#         res += 1
#     elif re.fullmatch(r'(beegeek)', i):
#         res += 2
# print(res)


# data = [line.strip() for line in sys.stdin]
# pat1 = r'(bee).*(bee)'
# pat2 = r'\b(geek)\b'
# bee = 0
# geek = 0
# for i in data:
#     if re.search(pat1, i):
#         bee += 1
#     if re.search(pat2, i):
#         geek += 1
# print(bee, geek, sep='\n')


# data = [line.strip() for line in sys.stdin]
# pattern = r'\b(\w*)\1\b'
# for i in data:
#     if re.fullmatch(pattern, i.strip()):
#         print(i.strip())
# or
# data = [line.strip() for line in sys.stdin]
# pattern = r'\b(\w*)\1\b'
# res = []
# for i in data:
#     match = re.search(pattern, i)
#     res.append(match.group())
# for i in res:
#     if len(i) > 1:
#         print(i)



# data = [line.strip() for line in sys.stdin]
# pattern = r'\_\d{1,}[a-zA-Z]{0,}\_?'

# for i in data:
#     print(True if re.fullmatch(pattern, i) else False)


# data = [line.strip() for line in sys.stdin]
# pattern = r'(\d{1,3})([- ])(\d{1,3})\2(\d{4,10})'

# for i in data:
#     match = re.search(pattern, i)
#     print(f'Код страны: {match.group(1)}, Код города: {match.group(3)}, Номер: {match.group(4)}')


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