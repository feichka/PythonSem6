# 1.	Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Введите натуральное число '))
lst = [i for i in range(1, n + 1)]
print(lst)
def f(n):
   return [3*i + 1 for i in range(1,n+1)]
dict = list(zip(lst, f(n)))
my_dict = {dict[i][0]: dict[i][1] for i in range(len(dict))}
print(my_dict)
