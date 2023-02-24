# import functools


# class MaxRetriesException(Exception):
#     pass

# def retry(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     pass
#             raise MaxRetriesException
#         return wrapper
#     return decorator




# def ignore_exception(*errors):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except errors as e:
#                     print(f'Исключение {e.__class__.__name__} обработано')
#         return wrapper
#     return decorator



# def add_attrs(**attr):
#     def decorator(func):
#         for k, v in attr.items():
#             func.__dict__[k] = v
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator



# def takes(*types):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in (*args, *kwargs.values()):
#                 if type(i) not in types:
#                     raise TypeError
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator




# def returns(datatype):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, **kwargs)
#             if type(val) != datatype:
#                 raise TypeError
#             return val                
#         return wrapper
#     return decorator



# def strip_range(start, end, char='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, **kwargs)
#             if end > len(val):
#                 val = val[:start] + char * (len(val) - start)
#             else:
#                 val = val[:start] + char * (end - start) + val[end:]
#             return val
#         return wrapper
#     return decorator



# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, times + 1):
#                 val = func(*args, **kwargs)
#             return val
#         return wrapper
#     return decorator



# def make_html(tag):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#         return wrapper
#     return decorator



# def prefix(string: str, to_the_end: bool=False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if to_the_end:
#                 return func(*args, **kwargs) + string
#             return string + func(*args, **kwargs)
#         return wrapper
#     return decorator



# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'TRACE: вызов {(func.__name__)}() с аргументами: {args}, {kwargs}')
#         res = func(*args, **kwargs)
#         if type(res) == str:
#             print(f"TRACE: возвращаемое значение {(func.__name__)}(): '{res}'")
#         else:
#             print(f"TRACE: возвращаемое значение {(func.__name__)}(): {res}")
#         return res
#     return wrapper



# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if type(func(*args, **kwargs)) == str:
#             return func(*args, **kwargs)
#         else:
#             raise TypeError
#     return wrapper



# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)**2
#     return wrapper
        


# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if i <= 0:
#                 raise ValueError
#             elif type(i) != int:
#                 raise TypeError
#         for k, v in kwargs.items():
#             if v <= 0:
#                 raise ValueError
#             elif type(v) != int:
#                 raise TypeError
#         return func(*args, **kwargs)
#     return wrapper




# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             return (res, 'Функция выполнилась без ошибок')
#         except:
#             return (None, 'При вызове функции произошла ошибка')
#     return wrapper

# def reverse_args(func):
#         def wrapper(*args, **kwargs):
#             args = [i for i in args][::-1]
#             # args.reverse()
#             res = func(*args, **kwargs)
#             return res
#         return wrapper


# @reverse_args
# def operation(a, b):
#     return a // b
    
# print(operation(90, 0))



# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     d = {}
#     d.setdefault('name', grades['name'])
#     d['top_grade'] = max(grades['grades'])
#     return d
    



# print(*top_grade.__annotations__.values())




# from datetime import datetime, date


# d = {'ru': '%d.%m.%Y',
#      'us': '%m-%d-%Y',
#      'ca': '%Y-%m-%d',
#      'br': '%d/%m/%Y',
#      'fr': '%d.%m.%Y',
#      'pt': '%d-%m-%Y',}

# def date_formatter(country_code):
#     def func(date):
#         return datetime.strftime(date, d[country_code])
#     return func


# date_ru = date_formatter('ru')
# today = date(2022, 1, 25)
# print(date_ru(today))


# def sourcetemplate(url):
#     def f1(**kwargs):
#         if not kwargs:
#             return url
#         s = ''
#         for k, v in sorted(kwargs.items()):
#             s += str(k) + '=' + str(v) + '&'
#         return url +'?' + s[:-1]
#     return f1


# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
# print(*sorted(map(lambda x: x.title(), filter(lambda x: len(x) > 4 and x[0].lower() in ('а', 'м'), names))))



# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
# print(*map(lambda x: x**2, filter(lambda x: x in range(-99, 100) and not x % 9, numbers)))



# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]

# print(*map(int, filter(lambda x: type(x) is int or type(x) is float, data)), sep='\n')