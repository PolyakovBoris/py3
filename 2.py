# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import collections

with open("article.txt", encoding="utf-8") as file: # статья из файла
    text = file.read()

word_counter = dict()

for item in text.split(): # итерация по словам с разделителем пробел
    if len(item) > 1: # исключаем союзы из одной буквы
        if item not in word_counter: # есть ли ключ со счётчиком по данному слову
            word_counter.setdefault(item) # если нет, создается ключ
            word_counter[item] = 0 # и значение 0
        word_counter[item] = int(word_counter.get(item)) + 1 # счётчик частоты слов

print(collections.Counter(word_counter).most_common(10)) # метод most_common с аргументом 10 сортирует и
                                                        # первые отбирает 10 элементов
