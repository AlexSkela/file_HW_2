def add_files(files_list):
    text_dict = {}
    for file in files_list:
        with open(file, encoding='utf-8') as f:
            file_text = f.readlines()
            text_dict[len(file_text)] = (file, ' '.join(file_text))

    text_dict = dict(sorted(text_dict.items()))


    with open('finish_fail.txt', 'w', encoding='utf-8') as new:
        for file, text in text_dict.items():
            new.write(f'{text[0]} \n')
            new.write(f'{file} \n')
            new.write(f'{text[1]}')


files = ['1.txt', '2.txt', '3.txt']
add_files(files)


