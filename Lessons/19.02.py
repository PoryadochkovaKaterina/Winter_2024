# Задание 15-1
# dic =   {1: {1: 11111,
#              2: 22222,},
#         2: 2,
#         3: {4: 11,
#            5: 33,
#            2: 22,
#            3: {1: 111,
#               2: 222,
#               3: {3: 1111,
#                  1: 2222,
#                  'a': 3333,
#                  4: {1: 555,
#                     2: 666,}},
#               4: 44,},
#             1: 55,},
#         'm': 4}
#
# def dct_val(dic, x):
#     r = []
#     for k, v in dic.items():
#         if k == x:
#             r.append(v)
#         if type(v) == dict:
#             s = dct_val(v, x)
#             r.extend(s)
#     return r
# print(dct_val(dic, 1))

# Задание 15-2
# import re
# ab = 'АВКЕМНОРСТУХABEKMHOPCTYXD'
# tm = r'[АВКЕМНОРСТУХABEKMHOPCTYXD]\d{3}[АВКЕМНОРСТУХABEKMHOPCTYXD]{2}{1}?78'
# s = input()
# re.findall(tm, s)

# import re
# abc = 'АВКЕМНОРСТУХABEKMHOPCTYXD'
# tmp1 = rf"[{abc}]\d\d\d[{abc}{abc}][1]?78"
# ss = input()
# print(re.findall(tmp1, ss))

# RE
# \b\w{3}\b   # слово точно из 3 букв
# [+-]?\d+   # целое число со знаком

# import re
# text = 'fizz.123.buzz.456.fizzbuzz'
# res1 = re.sub(r'\d', r'#', text)
# res2 = re.sub(r'[a-z]+', r'(*)', text)
# print(res1)
# print(res2)


# !!! HABR регулярки в Python !!!


# import re
# def fullname(x):
#     s = x.group()   # x-специальный объект, который содержит значение, индекс начала и конца
#     print(x.group(), x.start(), x.end())
#     # if s == 'Коля': return 'Николай'
#     # elif s == 'Миша': return 'Михаил'
#     # else: return '*****'
#     match s:   # Замена if, elif, else
#         case 'Коля': return 'Николай'   # 12 - индекс начала, 16 индекс конца 'Коля'. Следующий за
#         case 'Миша': return 'Михаил'   # 26 - индекс начала, 30 индекс конца 'Миша'. Следующий за
#         case _: return '******'
# text = 'Здравствуй, Коля! Привет, Миша, это Петя'
# print(re.sub(r'\b\w{4}\b', fullname, text))

# import re
# def art(x):
#     s = x.group()
#     print(x.group(), x.start(), x.end())
#     # dct = {'LED': 'Пулково',
#     #        'MSQ': 'Минск',
#     #        'SVO': 'Шерементьево',
#     #        'SVX': 'Кольцово'}
#     # return dct.get(s, '?')
#     match s:
#         case 'LED': return 'Пулково'
#         case 'MSQ': return 'Минск'
#         case 'SVO': return 'Шерементьево'
#         case 'SVX': return 'Кольцово'
#         case _: return '?'
# text = 'Самолет вылетел из LED, пролете мимо SVO и приземлился в SVX'
# print(re.sub(r'\b\w{3}\b', art, text))

# import re
# text = 'first second'
# print(re.sub(r'(\w+) (\w+)', r'\2 \1', text))   # поменять местами second first
# print(re.sub(r'(\w+) (\w+)', r'\1 \1 \2 \2', text))   # дублирование слов first first second second
# print(re.sub(r'(\w+) (\w+)', r'\1+\1 \2:\2', text))   # дублирование слов first+first second:second

# import re
# text = 'Ким Катерина Дмитриевна'
# print(re.sub(r'(\w+) (\w+) (\w+)', r'\2 \3 \1', text))

# import re
# text = ('Программа на Java транслируется на байт-код java, выполняемый'
#         'виртуальной машиной Java(JVM) - программой, обрабатывающей '
#         'байтовый код и передающей инструкции оборудования как интерпритатор.')
# res = re.sub(r'Java', r'Python', text, count=2, flags=re.I)   # флаг re.I - игнорирует маленькие и большие буквы
# # count - управляет количеством замен, если count нет, то меняет все слова
# print(res)

# import re
# text = '123 first 345 second'
# print(re.findall(r'\d+ (\w+)', text))   # ['first', 'second']
# # если в шаблоне несколько скобок, то выдается список кортежей

# import re
# text = 'Миша:123 Коля:234 Сеня:354'
# res = re.findall(r'(\w+):(\d+)', text)
# print(res)

# Выбор части текста,используя скобки в шаблоне
# import re
# text = 'www.itmo.ru, www.epam.com, www.tut.by, www.school.net'
# print(re.findall(r'www\.(\w+)\.(?:com|ru|by)', text))
# # ?: - выбор одного из вариантов

# RE.FINDITER()
# import re
# text = 'abracadabra'
# # res = re.finditer(r'a', text)   # все буквы а
# # res = re.finditer(r'[^a]', text)   # исключая а
# # res = re.finditer(r'[ab]', text)   # только a и b
# res = re.finditer(r'(ab)', text)   # только ab
# for i in res:
#     print(i.group(), i.start(), i.end())   # что, начиная с какого индекса, окончание каким индексом
#     print(text[i.start():i.end()])

# import re
# text = 'abracadabra'
# res = re.sub(r'a', r'A', text)
# print(res)
# cou = 0
# for i in res:
#     if i == 'A':
#         cou += 1
#         res1 = 'A' + str(cou)
#         print(res1)
#         print(re.sub(r'A', res1, res))


# def fu(text):
#     cou = 0
#     def chan(x):
#         nonlocal cou
#         cou += 1
#         return 'A' + str(cou)
#     return re.sub(r'a', chan, text)
# print(fu('abracadabra'))

# RE.SPLIT()
# import re
# text = '1   + 222 * 3 -    7 / 2'
# print(re.split(r'\D+', text))   # шинкует по всем не числовым символам
# print(re.split(r'\s+', text))   # шинкует по всем пробельным символам
# print(re.split(r'\w+', text))
# print(re.split(r'[ +*/-]+', text))
# print(re.split(r'[^\d]+', text))
# print(re.split(r'[ \d]+', text))

# RE.COMPILE()
# import re
# num = re.compile(r'\d+')   # компиляция шаблона, для использования в программе
#
# print(re.findall(num, 'Я живу в дом. 2 кв. 13'))   # Способ 1 для вызова шаблона
# print(num.findall('Читаю стр. 234, абзац 9'))   # Способ 2 для вызова шаблона

# Совместное использование r и f
# import re
# x = 5
# # print(re.findall(fr'{x}', '112233445566'))   # поиск всех 5-рок (всех х)
# # print(re.findall(fr'{str(x)*2}', '112233445566'))   # поиск все 5-ок стоящий рядом (x{2})
# res = '|'.join(str(i) for i in range(x))   # поиск всех строковых значений в диапозоне от i до x
# res += '|' + 'abc'
# print(re.findall(fr'{res}', '112abc233445abc566'))

# ДЕКОРАТОРЫ
# def декоратор(декорируемая функция):
#     def Обертка():
#         Действия до вызова
#         Декорируемая функция
#         Действия после вызова
#         return
#     return Обертка

# def func(f):
#     return f
# def hello():
#     print('Привет!!!')
# # hello()   # вывоз функции hello
# # func(hello)   # передача функции hello как параметра в функцию func, после вызова hello
# # hello() + func(hello) -> func(hello)()
# func(hello)()  # передача функции hello как параметра без дополнительного вызова hello


# def speak(text):
#     def whis(t):   # определение новой функции
#         return t.lower()   # перевод в нижний регистр
#     res = whis(text)   # вызываем новую функцию
#     return res   # возвращаем функцию whis как результат speak
# print(speak('HELLO, WORLD!'))

# def speak():
#     def whisper(t):
#         return t.lower() + '...'
#     return whisper   # функция не вызывается, а возвращается
# wr = speak()   # получаем из функции speak объект функции whisper
# print(wr('HELLO, WORLD!'))   # вызываем функцию с одним агрументом

# def null_dec(func):
#     return func   # возвращение самой функции
# def hello():
#     print('Hello world!')
# hello = null_dec(hello)   # декорирование функции hello
# # передаем в качестве параметра hello в func
# # изменяем функцию и передаем её на вход
# hello()

# def samp_dec(func):   # определение декоратора
#     def wra():
#         print('Начало')
#         func()   # обертываем func, не вмещиваясь в ее работу
#         print('Конец')
#         return
#     return wra   # данный return относится к samp_dec, а не к wra
# def say():
#     print('Hello world!')
#
# say = samp_dec(say)   # декорируем функцию
# say()   # вызываем декорируемую функцию

# При вызове фукнции samp_dec(say) с переданной в качестве аргумента фукнцией say()
# возвращается вложенная функция wra() в качестве результат

# def goodbay():
#     print('Good Bye')
# goodbay()
# goodbay = samp_dec(goodbay)
# goodbay()
#
# abc = print   # abc работает как print
# abc(123)

# abc = input   # abc работает как input
# print(abc())


# def samp_dec(func):   # определение декоратора
#     def wra():
#         print('Начало')
#         func()   # обертываем func, не вмещиваясь в ее работу
#         print('Конец')
#         return
#     return wra   # данный return относится к samp_dec, а не к wra, но возвращает wra
# # @samp_dec
# def say():
#     print('Hello world!')
# say = samp_dec(say)
# print(say())

def upper(func):
    def wrap():
        orig_res = func()
        # mod_res = orig_res.title()   # делает все первые буквы большими, а остальные маленькими (во всех словах)
        # mod_res = orig_res[::-1]   # в обратном порядке
        # mod_res = ' '.join(orig_res.split()[::-1])   # обратный порядок слов

        return mod_res
    return wrap
# @upper
def h():
    return 'Hello world and all'
h = upper(h)
print(h())

# @upper == h = upper(h)