



# лабораторна номер 3 завдання 18
def sequence_conversion(my_list):

    if my_list == my_list[::-1]:
        return my_list
    par = []
    ne_par = []
    for i in range(0, len(my_list)):
        if i % 2 == 0:
            par.append(my_list[i])
        else:
            ne_par.append(my_list[i])

    result = []
    result.extend(ne_par)
    result.extend(par)
    return result


a = sequence_conversion([1, 2, 3, 4, 5, 6, 56, 33, 12, 77, 5, 101])


for i in range(len(a)):
    print(a[i], end=' ')
    if (i + 1) % 5 == 0:
        print()


