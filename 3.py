# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант

stuff_dict = {'torch': 5, 'tent': 10, 'rifle': 6, 'hat': 1, 'firstaidKit': 2, 'knife': 1, 'map': 1}
get_stuff = dict() # словарь взятых предметов
max_load = 12
weight = 0
reserve_weight = 12
for key, value in stuff_dict.items(): # перебор словаря предметов
    print(key, value)
    if value <= reserve_weight: # если осталось место кладем в рюкзак
        weight += value
        get_stuff[key] = value
        reserve_weight -= value
print(get_stuff)
