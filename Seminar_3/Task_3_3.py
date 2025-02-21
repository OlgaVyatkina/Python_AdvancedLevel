'''
Задание №3
Погружение в Python | Коллекции
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа
'''


import pprint
my_dict1 = {}
my_dict2 = {}

my_typle = (1, 2, "a", [1, 2, 3], 4.5, True, False, True)
for i in my_typle:
    my_dict1.setdefault(type(i), []).append(i)           #верный результат (здесь значение словаря - список)
    my_dict2.setdefault(type(i), i)                     #неверный результат

pprint.pprint(my_dict1)                                # для словарей очень удобно
print(my_dict1)                                          # верный результат
print(my_dict2)                                         # неверный результат



my_typle = (1, 2, "a", [1, 2, 3], 4.5, True, False, True)
my_dict = {}
for i in my_typle:
    my_dict.setdefault(type(i), []).append(i) 
[print(f'{key}, {value}') for key, value in my_dict.items()]
