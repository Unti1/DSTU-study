# алгоритм Хаффмана.
from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

# Получения шифра
def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes

# Создание древа
def get_tree(string):
    string_count = Counter(string) # подсчет частоты повторений

    if len(string_count) <= 1:
        node = Node(None)
        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)
        
        string_count = {node: 1}
    

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1] # наиболее часто встречаемые символы в  порядке убывания 
        # print(spam)
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]

# Кодирование
def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res

# Декодирование
def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res



with open('testout/file1.txt',"r",encoding="utf-8") as f:
    file_text = f.read()
# создаем дерево по данным файла 
tree = get_tree(file_text)
# создаем шифр под символ
codes = get_code(tree)
# print(f'Шифр: {codes}')

# сжимаем данные файла1 в файл2 
coding_text = coding(file_text, codes)
# print('Сжатая строка: ', coding_text)
with open('testout/file2.txt',"w",encoding='utf-8') as f:
    f.write(coding_text)


decoding_text = decoding(coding_text, codes)
# print('Исходная строка: ', decoding_text)
with open('testout/file3.txt',"w",encoding='utf-8') as f:
    f.write(decoding_text)

# Проверка на точность перевода
with open("testout/file1.txt",'r',encoding='utf-8') as f:
    with open ("testout/file1.txt",'r',encoding='utf-8') as f1:
        text1 = f.read()
        text2 = f1.read()
        if text1 == text2:
            print("Успех")
        else:
            print("Неудача")