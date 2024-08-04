immutable_var = 1, 2, 'a', 'b', True, [1, 2, 3]
print('Immutable tuple: ', immutable_var)

# immutable_var[0] = 10
# кортеж не поддерживает изменение элементов

mutable_list = [1, 2, 'a', 'b']
mutable_list.append("Modified")
print('Mutable list: ', mutable_list)