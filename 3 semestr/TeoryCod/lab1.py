# алгоритм Хаффмана.
from collections import Counter
import pickle
# Узлы для построения древа
# Переменные left и right отображают сторону в которую пойдет ветвление узла (Право или Лево)
class Node: 
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

# Создание древа
def get_tree(text):
    text_count = Counter(text) # подсчет частоты повторений

    if len(text_count) <= 1:
        node = Node(None) # Задаем изначальный узел с пустым(None) значением

    
        if len(text_count) == 1:
            node.left = Node([key for key in text_count][0])
            node.right = Node(None)
            
        text_count = {node: 1}
    

    while len(text_count) != 1:
        node = Node(None)
        spam = text_count.most_common()[:-3:-1] # наиболее часто встречаемые символы в  порядке убывания 
        # Выборка в spam идет с конца по 2  элемента 
        # print(spam)
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]

        del text_count[spam[0][0]]
        del text_count[spam[1][0]]
        text_count[node] = spam[0][1] + spam[1][1]

    return [arg for arg in text_count][0]

# Получения шифровки каждого символа
def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


# Кодирование
def coding(text, codes):
    res = ''

    for symbol in text:
        res += codes[symbol]
    return res.encode('utf-8')

# Декодирование
def decoding(text, codes):
    res = ''
    i = 0

    while i < len(text):

        for code in codes:

            if text[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])
    return res



with open('testout/file1.txt',"r",encoding="utf-8") as f:
    file_text = f.read()
# создаем дерево по данным файла 
tree = get_tree(file_text)
# создаем шифр под символ
codes = get_code(tree)
print(f'Шифр: {codes}')

# сжимаем данные файла1 в файл2 
coding_text = coding(file_text, codes)
# print('Сжатая строка: \n', coding_text)
with open('testout/file2.dat',"wb") as f:
    pickle.dump(coding_text,f)

decoding_text = decoding(coding_text.decode('utf-8'), codes)
# print('Исходная строка: ', decoding_text)
with open('testout/file3.txt',"w") as f:
    f.write(decoding_text)

# Проверка на точность перевода
with open("testout/file1.txt",'r',encoding='utf-8') as f:
    with open ("testout/file2.txt",'r',encoding='utf-8') as f1:
        text1 = f.read()
        text2 = f1.read()
        if text1 == text2:
            print("Успех")
        else:
            pass
            # print("Неудача")





# Создать меню 
# Информацию о 0 и 1 в битовую
# В конец второго файла дописать вероятности
# В декодировании считывать вероятности и строить дерево заного 