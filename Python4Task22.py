print('''
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
''')


import random
n = int(input("Введите размер первого набора целых чисел: "))
m = int(input("Введите размер второго набора целых чисел: "))

# array_1=[]
# array_2=[]
# array_3=[]

array_1=array_2=array_3=[] # Значения из списка 1 сразу будут внесены в список 2 и он будет долняться новыми m элементами

for i in range(n):
    array_1.append(random.randint(1,1000))
print (array_1)

for i in range(m):
    array_2.append(random.randint(1,1000))
print (array_2)

# array_3 = array_1 + array_2
array_3 = set(array_3)
print (sorted(array_3))
