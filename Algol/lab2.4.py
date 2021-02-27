import string

filename = 'sym2.txt'


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

# print(finder(filename,"G"))

def uni_word(filename):
    with open(filename,"r",encoding='utf8') as f:
        filetxs = f.readlines()

    u_dict = []

    for i in range(len(filetxs)):
        filetext = filetxs[i]
        filetext.translate(str.maketrans('', '', string.punctuation))
        for j in range(len(filetext.split(' '))):
            