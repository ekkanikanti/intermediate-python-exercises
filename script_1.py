def get_unique_list(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)