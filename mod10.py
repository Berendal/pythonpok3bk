def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as f:
        l = (i.split('\n') for i in f.read().split('\n\n'))
        m = tuple(j.split('=') for j in l for i in l)
        print(m)

planets = txt_to_dict()

print(next(planets))





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