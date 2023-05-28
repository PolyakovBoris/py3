# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [4, 2, 3, 1, 4, 3, 4, 1, 4, 6, 9, 9, 9]
numbers_dublicate = [] # список дубликатов


for counter in range(len(my_list)): # итерируемся количество раз равное длине списка
    num_to_compare = my_list[counter] # берем последовательно число для поиска дубликатов

    for elem in range(counter + 1, len(my_list)):# итерируемся по списку
        if my_list[elem] == num_to_compare and my_list[elem] not in numbers_dublicate: # если дубликат и он ещё не в новом списке
            numbers_dublicate.append(num_to_compare) # добавляем в список дубликатов

            break # прерываем итерацию, чтобыв список повторно не попал сравниваемый элемент

print(numbers_dublicate)
# for i in numbers_to_remove:
#     my_list.remove(i)
# print(my_list)

#
# user_input = input('input something')
# if user_input.isdigit() is True:
#     print('yes')
#     if int(user_input) >= 0:
#         user_intput = int(user_input)
#         print(f'int {user_input}')
#
# elif user_input.count('.') > 0 and user_intput >= 0:
#     user_input = float(user_input)
#     print(f'float {user_input}')
#
# elif user_input.islower() is not True:
#     user_input = user_input.lower();
#     print(f'была заглавная {user_input}')
#
# else:
#     print(user_input.upper())

# my_tuple = (1, '2', 'Hello', 2.2, 'jkghj', 2, 2, 22222, -456)
# my_dict = dict()
#
# for i in my_tuple:
#     print(i)
#     tmp_list = []
#
#     my_dict.setdefault(type(i))
#     print(my_dict)
#     print(my_dict.get(type(i)))
#     if my_dict.get(type(i)) is not None:
#         tmp_list = my_dict.get(type(i))
#     print(tmp_list)
#     tmp_list.append(i)
#     my_dict[type(i)] = tmp_list
#
# print(my_dict)
#
# user_input = 'это новая строка юзера'
# for num, word in enumerate(sorted(user_input.split()), start=1):
#     print(f'{num} {word:>5}')

