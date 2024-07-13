# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = [1, 'e', True]
values_dict = {'a': 4, 'b': 'w', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [5, 's']
print_params(*values_list_2, 42)