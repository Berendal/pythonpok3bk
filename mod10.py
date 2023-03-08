# from itertools import product, chain
# from string import digits, ascii_uppercase

# n, m = int(input()), int(input())

# lst = list(chain(map(str, digits), ascii_uppercase))

# for i in product(lst[:n], repeat=m):
#     print(*i, sep='', end=' ')


# def password_gen():
#     for i in product(range(10), repeat=3):
#         yield str(i[0]) + str(i[1]) + str(i[2])


# from string import ascii_lowercase
# from itertools import product

# letters = ascii_lowercase[:8]
# digits = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in product(letters, digits):
#     print(*i, sep='', end=' ')




# from collections import namedtuple
# import itertools

# Item = namedtuple('Item', ['name', 'mass', 'price'])

# items = [Item('Обручальное кольцо', 7, 49_000),
#          Item('Мобильный телефон', 200, 110_000),
#          Item('Ноутбук', 2000, 150_000),
#          Item('Ручка Паркер', 20, 37_000),
#          Item('Статуэтка Оскар', 4000, 28_000),
#          Item('Наушники', 150, 11_000),
#          Item('Гитара', 1500, 32_000),
#          Item('Золотая монета', 8, 140_000),
#          Item('Фотоаппарат', 720, 79_000),
#          Item('Лимитированные кроссовки', 300, 80_000)]


# weight = int(input())
# try:
#     goods = (max(filter(lambda x: sum(list(zip(*x))[1]) <= weight, (v for r in range(1, len(items) + 1) for v in itertools.combinations(filter(lambda x: x[1] <= weight, items), r))), key=lambda x: sum(list(zip(*x))[2])))
#     for i in sorted(goods):
#         print(i[0])
# except:
#     print('Рюкзак собрать не удастся')


# from itertools import combinations_with_replacement


# wallet = [100, 50, 20, 10, 5]

# count = 0
# for i in range(21):
#     for j in set(combinations_with_replacement(wallet, i)):
#         if sum(j) == 100:
#             count += 1
# print(count)


# from itertools import combinations


# wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

# count = 0
# for i in range(len(wallet)):
#     for j in set(combinations(wallet, i)):
#         if sum(j) == 100:
#             count += 1
# print(count)   


# from itertools import permutations


# for i in sorted(set(permutations(input()))):
#     print(*i, sep='')


# from itertools import groupby


# def ranges(numbers):
#     gi = groupby(sorted(enumerate(numbers), key=lambda x: x[1] - x[0]), key=lambda x: x[1] - x[0])
#     res = []
#     a = []
#     b = []
#     min_r = []
#     max_r = []
#     for k, v in gi:
        # res.append(list(v))
    # for i in res:
    #     a.append(min(i))
    #     b.append(max(i))
    # for i in a:
    #     min_r.append(i[1])
    # for i in b:
    #     max_r.append(i[1])
    # return [*zip(min_r, max_r)]


# def group_anagrams(words):
#     gi = groupby(sorted(words, key=sorted), key=sorted)
#     for k, v in gi:
#         yield (tuple(v))


# tasks = [('Отдых', 'поспать днем', 3),
#         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
#         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
#         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
#         ('Отдых', 'погулять вечером', 4),
#         ('Курс по ооп', 'обсудить темы', 1),
#         ('Урок по groupby', 'добавить задачи на программирование', 3),
#         ('Урок по groupby', 'написать конспект', 1),
#         ('Отдых', 'погулять днем', 2),
#         ('Урок по groupby', 'добавить тестовые задачи', 2),
#         ('Уборка', 'убраться в ванной', 2),
#         ('Уборка', 'убраться в комнате', 1),
#         ('Уборка', 'убраться на кухне', 3),
#         ('Отдых', 'погулять утром', 1),
#         ('Курс по ооп', 'обсудить задачи', 2)]

# gi = groupby(sorted(tasks, key=lambda x: x[0]), key=lambda x: x[0])
# for k, v in gi:
#     print(f'{k}:')
#     for i in sorted(v, key=lambda x: x[2]):
#         print(f'    {i[2]}. {i[1]}')
#     print()



# n = 'hello beegeek stepik python'.split()
# gi = groupby(sorted(n, key=len), key=len)
# for k, v in gi:
#     print(f'{k} -> {", ".join(i for i in sorted(v))}')


# from collections import namedtuple
# from itertools import groupby

# Student = namedtuple('Student', ['surname', 'name', 'grade'])

# students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]


# gi = groupby(sorted(students, key=lambda x: x[1]))
# res = [i for i in max(gi)]
# print(res[0].name)


# from collections import namedtuple
# from itertools import groupby

# Person = namedtuple('Person', ['name', 'age', 'height'])

# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]

# gi = groupby(sorted(persons, key=lambda x: x[2]), key=lambda x: x[2])

# for k, v in gi:
#     print(f'{k}: {", ".join(str(i.name) for i in sorted(v))}')


# from itertools import zip_longest, repeat


# def grouper(iterable, n):
#     a = iter(iterable)
#     return zip_longest(*repeat(a, n))
        


# from itertools import chain, tee


# def ncycles(iterable, times):
#     for i in tee(chain(iterable), times):
#         yield from i


# from itertools import pairwise


# def max_pair(iterable):
#     return max(a + b for a, b in pairwise(iterable))


# def is_rising(iterable):
#     return (all(a < b for a, b in pairwise(iterable)))



# from itertools import chain


# def sum_of_digits(iterable):
#     return sum(int(i) for i in chain.from_iterable(map(str, iterable)))

# def sum_of_digits(iterable):
#     res = []
#     for i in chain.from_iterable(map(str, iterable)):
#         res.append(int(i))
#     return sum(res)

# print(sum_of_digits([123456789]))



# from itertools import dropwhile


# def first_largest(iterable, number):
#     data = [i for i in iterable]
#     res = []
#     for i in dropwhile(lambda x: x <= number, data):
#         res.append(i)
#     try:
#         return data.index(res[0])
#     except IndexError:
#         return -1


# from itertools import islice


# def take_nth(iterable, n):
#     for i in islice(iterable, n - 1, n):
#         return i


# from itertools import islice


# def take(iterable, n):
#     yield from islice(iterable, n)


# def first_true(iterable, predicate):
#     for i in filter(predicate, iterable):
#         return i


# from itertools import dropwhile


# def drop_this(iterable, obj):
#     yield from dropwhile(lambda n: n == obj, iterable)



# from itertools import dropwhile


# def drop_while_negative(iterable):
#     yield from dropwhile(lambda it: it < 0, iterable)



# def roundrobin(*args):
#     yield from (i for arg in it.zip_longest(*args, fillvalue='*') for i in arg if i != '*')
    # data = it.zip_longest(*args, fillvalue='*')
    # res = []
    # for i in data:
    #     for j in i:
    #         if j != '*':
    #             res.append(j)
    # return iter(res)


# import string


# letters = string.ascii_uppercase
# def alnum_sequence():
#     generator = (char for obj in zip(it.count(1), letters) for char in obj)
#     cycle = it.cycle(generator)
#     yield from cycle



# import operator


# def factorials(n):
#     yield from it.accumulate(range(1, n + 1), operator.mul)


# def tabulate(func):
#     yield from map(func, it.count(1))


# def around(iterable):
#     data = [i for i in iterable]
#     a = [None] + data[:-1], data, data[1:] + [None]
#     yield from list(zip(*a))


# def pairwise(iterable):
#     data = [i for i in iterable]
#     a = data, data[1:] + [None]
#     yield from list(zip(*a))


# def with_previous(iterable):
#     data = [i for i in iterable]
#     a = data, [None] + data[:-1]
#     yield from list(zip(*a))


# def stop_on(iterable, obj):
#     for i in iterable:
#         if i == obj:
#             break
#         yield i



# from collections import Counter


# def unique(iterable):
#     yield from Counter(iterable)




# def txt_to_dict():
#     with open('planets.txt', 'r', encoding='utf-8') as f:
#         l = (i.split('\n') for i in f.read().split('\n\n'))
#         m = (i.split('=') for j in l for i in j)
#         d = {}
#         for _ in range(5):
#             for i in m:
#                 d.setdefault(i[0].strip(), i[1].strip())
#                 if len(d) == 4:
#                     yield d
#                     d = {}





# def nonempty_lines(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f.readlines():
#             l = (i if len(i) <= 25 else '...' for i in line.split() if not i.isspace())
#             yield from l


# from datetime import date, timedelta


# def years_days(year):
#     d = date(year, 1, 1)
#     while d.year == year:
#         yield d
#         d += timedelta(days=1)



# from datetime import date, timedelta

# def dates(start, count=None):
#     try:
#         if count is None:
#             count = 0
#             while True:
#                 yield start + timedelta(count)
#                 count += 1
#         else:
#             for i in range(count):
#                 yield start + timedelta(i)
#     except OverflowError:
#         StopIteration




# with open('data.csv', 'r', encoding='utf-8') as f:
#     file_lines = (line for line in f)
#     line_values = (line.rstrip().split(',') for line in file_lines)
#     file_headers = next(line_values)
#     line_dicts = (dict(zip(file_headers, data)) for data in line_values)
#     res = (i['raisedAmt'] for i in line_dicts if i['round'] == 'a')
#     a = []
#     for i in res:
#         a.append(int(i))
#     print(sum(a))




# def filter_names(names, ignore_char, max_names):
#     gen = (i for i in names if i[0] != ignore_char.upper() and i.isalpha())
#     gen2 = (i for _, i in zip(range(max_names), gen))
#     yield from gen2
    



# def parse_ranges(ranges):
#     rang = (i.split('-') for i in ranges.split(','))
#     rang1 = (range(int(i[0]), int(i[1]) + 1) for i in rang)
#     return (i for j in rang1 for i in j)
        

# from collections import namedtuple

# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

# swed = (i for i in persons if i.nationality == 'Swedish')
# swedalive = (i for i in swed if i.death == 0)
# swedm = (i for i in swedalive if i.sex == 'male')
# res = []
# for i in sorted(swedm, key=lambda x: x[3], reverse=True):
#     res.append(i.name)
# print(res[0])


# def interleave(*args):
#     return (i for j in zip(*args) for i in j)


# def all_together(*args):
#     return (i for j in args for i in j)


# def count_iterable(iterable):
#     gen = (i for i in iterable)
#     count = 0
#     for _ in gen:
#         count += 1
#     return count



# def is_prime(number):
#     return False if number == 1 else all(number % n for n in range(2, number))


# def is_prime(number):
#     if number == 1:
#         return False
#     else:
#         gen = (i for i in range(2, number) if number % i == 0)
#         try:
#             next(gen)
#             return False
#         except:
#             return True


# def cubes_of_odds(iterable):
#     return (num ** 3 for num in iterable if num % 2)



# def flatten(nested_list):
#     for i in nested_list:
#         if type(i) == list:
#             yield from flatten(i)
#         else:
#             yield i


# def palindromes():
#     yield from (i for i in range(1, 9999999) if str(i) == str(i)[::-1])



# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row



# def card_deck(suit):
#     card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
#     card_suits = ["пик", "треф", "бубен", "червей"]
#     card_suits.remove(suit)
#     while True:
#         for i in card_suits:
#             for j in (card_values):
#                 yield f'{j} {i}'



# from datetime import date, timedelta

# def dates(start, count=None):
#     try:
#         if count is None:
#             count = 0
#             while True:
#                 yield start + timedelta(count)
#                 count += 1
#         else:
#             for i in range(count):
#                 yield start + timedelta(i)
#     except OverflowError:
#         StopIteration




# def reverse(sequence):
#     for i in sequence[::-1]:
#         yield i



# def primes(left, right):
#     for i in range(left, right + 1):
#         count = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count += 1
#         if count == 2:
#             yield i



# def alternating_sequence(count=None):
#     if count is None:
#         count = 1
#         while True:
#             yield - count if count % 2 == 0 else count
#             count += 1
#     else:
#         for i in range(1, count + 1):
#             yield - i if i % 2 == 0 else i
    



# def simple_sequence():
#     number = 1
#     while True:
#         for _ in range(number):
#             yield number
#         number += 1




# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.start = start - step
#         self.end = end
#         self.step = step

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.step > 0:
#             self.start += self.step
#             if self.start >= self.end:
#                 raise StopIteration
#         if self.step < 0:
#             self.start += self.step
#             if self.start <= self.end:
#                 raise StopIteration
#         return self.start
        
# xrange = Xrange(5, 10)

# print(*xrange)

# class Alphabet:
#     def __init__(self, language):
#         self.language = language
#         self.index = -1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         lang = {'ru': [chr(i) for i in range(1072, 1104)], 'en': [chr(i) for i in range(97, 123)]}
#         self.index += 1
#         if self.index < len(lang[self.language]):
#             return lang[self.language][self.index]
#         else:
#             self.index = 0
#             return lang[self.language][self.index]

# en_alpha = Alphabet('en')

# for _ in range(40):
#     next(en_alpha)

# for _ in range(40):
#     next(en_alpha)

# for _ in range(40):
#     next(en_alpha)

# print(next(en_alpha))


# from random import randint


# class RandomNumbers:
#     def __init__(self, left, right, n):
#         self.left = left
#         self.right = right
#         self.n = n
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         res = randint(self.left, self.right)
#         self.index += 1
#         if self.index <= self.n:
#             return res
#         else:
#             raise StopIteration


# iterator = RandomNumbers(-1000, -900, 1)

# print(next(iterator) in range(-1000, -899))

# try:
#     next(iterator)
# except StopIteration:
#     print('Error')


# class Cycle:
#     def __init__(self, iterable):
#         self.iter = iterable
#         self.index = -1


#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 1
#         if self.index < len(self.iter):
#             return self.iter[self.index]
#         else:
#             self.index = 0
#             return self.iter[self.index]



# cycle = Cycle(range(100_000_000))

# print(next(cycle))
# print(next(cycle))

# class CardDeck:
#     def __init__(self):
#         self.length = 52
#         self.index = 0
#         self.suits = ['пик', 'треф', 'бубен', 'червей']
#         self.ranks = [*range(2, 11), 'валет', 'дама', 'король', 'туз']

    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= self.length:
#             raise StopIteration
#         suit = self.suits[self.index // len(self.ranks)]
#         rank = self.ranks[self.index % len(self.ranks)]
#         self.index += 1
#         return f'{rank} {suit}'


# cards = list(CardDeck())

# print(cards[9])
# print(cards[23])
# print(cards[37])
# print(cards[51])



# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         a = [i for i in self.data]
#         self.index += 1
#         if self.index > len(self.data):
#             raise StopIteration
#         return (a[self.index - 1], self.data[a[self.index - 1]])



# data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8], 
#         'Anri': [100, 101], 'Roma': [99]}

# pairs = DictItemsIterator(data)

# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))

# try:
#     print(next(pairs))
# except StopIteration:
#     print('Error')

# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.index = -1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.index += 1
#         return self.number ** self.index

# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.index = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         res = self.number ** self.index
#         self.index += 1
#         return res



# power_of_two = PowerOf(2)

# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))

# class Fibonacci:
#     def __init__(self):
#         self.index = 0
#         self.value = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index, self.value = self.value, self.index + self.value
#         return self.index


# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 1
#         if self.index > self.n:
#             raise StopIteration
#         return self.index**2


# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self.times = times
#         self.index = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 1
#         if self.index == self.times:
#             raise StopIteration
#         return self.obj


# class Repeater:
#     def __init__(self, obj):
#         self.data = obj

#     def __iter__(self):
#         return self

#     def __next__(self):
#         return self.data




# from random import randint


# def random_numbers(left, right):
#     return iter(lambda: randint(left, right), '')
    


# iterator = random_numbers(1, 10)

# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))
# print(next(iterator) in range(1, 11))

# def is_iterable(obj):
#     try:
#         iter(obj)
#         return True
#     except:
#         return False


# objects = [(1, 13), 7.0004, [1, 2, 3]]

# for obj in objects:
#     print(is_iterable(obj))


# def starmap(func, iterable):
#     return map(func, *zip(*iterable))



# points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

# print(*starmap(lambda x, y, z: x * y * z, points))



# from copy import copy


# def get_min_max(iterable):
#     iterable1 = copy(iterable)
#     try:
#         return (min(iterable), max(iterable1))
#     except:
#         return None