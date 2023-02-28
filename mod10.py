from random import randint


def random_numbers(left, right):
    return iter(lambda: randint(left, right), '')
    


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

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