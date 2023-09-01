def get_combined_dict(d1, d2):
    combined = {}
    for x in d1:
        for y in d2:
            if x == y and x not in combined:
                combined.update({x: d1[x] + d2[y]})
    return combined

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)