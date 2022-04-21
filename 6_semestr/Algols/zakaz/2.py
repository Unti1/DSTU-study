import os
import re




def find_suname(dct,suname):
    if dct[suname]:
        return(dct[suname])
    else:
        print("Фамилии не найдено")

def add_num():
    suname = input("Фамилия: ")
    number = input("Номер(в формате 0 000 000 00 00):")
    if re.fullmatch(r"\d{1} \d{3} \d{3} \d{2} \d{2}",number) != None:
        with open('db.txt','a',encoding='utf-8') as fl:
            fl.write(f"\n{suname},{number}")
    else:
        return 0

def safe_db(dct):
    with open("db.txt","w",encoding='utf-8') as fl:
        for key in dct.keys():
            fl.write(f"{key},{dct[key]}\n")

while True:

    if os.path.exists("db.txt"):
        dct = {}
        with open("db.txt",'r',encoding='utf-8') as fl:
            lines = fl.readlines()
            for line in lines:
                line = line.strip()
                suname,number = line.split(',') 
                dct[suname] = number
    else:
        fl = open('db.txt',"w")
        fl.close


    try:
        chooze = int(input("Выберите действие:\n1) Поиск по фамилии\n2) Добавить новый номер\n3) Cохранить базу и выйти\n"))
        if chooze == 1:
            sun = str(input("Введите фамилию челвоека:"))
            s = find_suname(sun)
            print(s)
        elif chooze == 2:
            add_num()
        elif chooze == 3:
            safe_db(dct)
            break
    
    except:
        pass
