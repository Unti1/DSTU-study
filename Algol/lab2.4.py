import string


def finder(filename,sym):
    with open(filename,"r",encoding='utf8') as f:
        filetxs = f.readlines()

    pos = []
    offset = len(sym)

    pogr = 0
    for i in range(len(filetxs)):
        
        filetext = filetxs[i].split('\n')[0]
        while filetext.find(sym) != -1:
            pos.append((i,filetext.find(sym)+ pogr))
            pogr += filetext.find(sym)
            filetext = filetext[filetext.find(sym) + offset :]
        pogr = 0
    return pos

print(finder("sym2.txt","G"))


def uni_word(filename):
    with open(filename,"r",encoding='utf8') as f:
        filetxs = f.readlines()

    u_dict = []
    dict_of_words = []

    for i in range(len(filetxs)):
        filetext = filetxs[i].split('\n')[0]
        filetext = filetext.translate(str.maketrans('', '', string.punctuation))
        list_of_word = filetext.split(' ')
        for j in range(len(list_of_word)):
            dict_of_words.append(list_of_word[j])

    my_dict = {i:dict_of_words.count(i) for i in dict_of_words}

    for val in my_dict.items():
        if val[1] == 1:
            u_dict.append(val[0])

    return u_dict

print(uni_word("sym3.txt"))

# доп задание текстовый файл с несколькими строчками , поменять местами 1 и последнюю не перезаписывая исходный файл(тоесть внутри внутри самого файла)