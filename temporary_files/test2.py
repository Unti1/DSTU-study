from collections import Counter
class Node: 
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value
#Жопа
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


filename1 = 'testout/file1.txt'

with open(filename1,"r",encoding="utf-8") as f:
    file_text = f.read()
# создаем дерево по данным файла 
tree = get_tree(file_text)
# создаем шифр под символ
codes = get_code(tree)
print('Шифры - ',codes)












with open('testout/file2.txt',"r") as f:
    text = f.read()
    textlist = text.split('\n')
    for_shifr = textlist[-1]
    # print(for_shifr)
    textlist.remove(textlist[-1])
    text = ''
    for i in textlist:
        text += i










# Выбираем список вероятностей из файла с шифром
shifr_list_1 = for_shifr.split('|')
shifr_list = []
def sortByNum(inputStr):
        return inputStr[1]
for val in shifr_list_1:
    if val != '':
        timeless_list = []
        timeless_list.append(val.split(':')[0])
        timeless_list.append(float(val.split(':')[1]))
        shifr_list.append(timeless_list)
shifr_list.sort(key=sortByNum,reverse=True)

print(shifr_list)




sum = 0
sum1 = 0
index_list = []
index_list1 = []
ent_list = []
for i in range(len(shifr_list)):
    if sum <= 0.5:
        index_list.append(i)
        sum += shifr_list[i][1]
        ent_list.append(shifr_list[i])
    else:
        index_list1.append(i)
        sum1 += shifr_list[i][1]
         
print(index_list,sum,sum1)       
