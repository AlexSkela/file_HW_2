
list_dict = {}
with open('1.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    list_dict['1.txt'] = data

with open('2.txt', 'r', encoding='utf-8') as g:
    data_1 = g.readlines()
    list_dict['2.txt'] = data_1

with open('3.txt', 'r', encoding='utf-8') as h:
    data_2 = h.readlines()
    list_dict['3.txt'] = data_2

print(list_dict)

with open('finish_fail.txt', 'w', encoding='utf-8') as new:
    for file, list_text in list_dict.items():
        new.write('\n')
        new.write(file)
        new.write('\n')
        for element in list_text:
            new.write(element)
            # new.write('\n')



