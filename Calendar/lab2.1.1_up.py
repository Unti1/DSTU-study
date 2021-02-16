# Написать программу предметная область - календарь
from datetime import datetime as dt , date , time , timedelta
import pandas

months = [
            [
                ['','Пн','Вт','Ср','Чт','Пт','Сб','Вс'],
                ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
            ],

            [
                [i for i in range(1,32)], #1
                [i for i in range(1,29)], #2
                [i for i in range(1,32)], #3
                [i for i in range(1,31)], #4
                [i for i in range(1,32)], #5
                [i for i in range(1,31)], #6
                [i for i in range(1,32)], #7
                [i for i in range(1,31)], #8
                [i for i in range(1,32)], #9
                [i for i in range(1,31)], #10
                [i for i in range(1,32)], #11 
                [i for i in range(1,31)]  #12
            ]
        ]

class Сalendar:

    def __init__(self,year,months):
        self.year = year
        self.months = months

    def get_calendar(self):
        

        greh = 0
        s=''
        spisok = []

        # +++ добавленный код
        year_of_mon = 2018

        for n in range(year_of_mon,self.year+1):
            if n % 4 == 0:
                greh += 2
            else:
                greh += 1
        
        if greh > 7:
            greh = greh/7
            
            if isinstance(greh,float):
                # если с плавающей точкой
                if greh < round(greh):
                    greh = round(greh) - 1
                else:
                    greh = round(greh)  
            elif isinstance(greh,int):
                # если число целочисленное 
                greh = greh
            spisok.append(greh)
        # +++  конец добавленного кода
        



        for i in range(len(months[1])):# вызов 12 раз
            print(months[0][1][i])  # Вывод месяца
            
            n1,n2,n3,n4,n5,n6,n7 = 1,2,3,4,5,6,7
            n1 += greh
            if n1 > 7 :
                n1 -= 7
            n2 += greh
            if n2 > 7 :
                n2 -= 7
            n3 += greh
            if n3 > 7 :
                n4 -= 7
            n4 += greh
            if n4 > 7 :
                n4 -= 7
            n5 += greh
            if n5 > 7 :
                n5 -= 7
            n6 += greh
            if n6 > 7 :
                n6 -= 7
            n7 += greh
            if n7 > 7 :
                n7 -= 7            

            days_of_the_week = months[0][0][n1]+"  "+months[0][0][n2]+"  "+months[0][0][n3]+"  "+months[0][0][n4]+"  "+months[0][0][n5]+"  "+months[0][0][n6]+"  "+months[0][0][n7]+"  "

            # !! 31 - (7*round(31/7)) формула для определения сдвига где 31 - количество ней января (должно быть len(mounths[1][i]))
            
            greh = len(months[1][i])-(7*round(len(months[1][i])/7))   # полученное значение
            spisok.append(greh)
            print(days_of_the_week) # Вывод дней недели
            
            if i == 1 and self.year % 4 == 0 : # условие февраля для високосный год
                months[1][i].append(29)

            for a in range(len(months[1][i])):
                if (a % 7 != 0 or a == 0)and(a != 6):
                    s+= f'{months[1][i][a]}'+"  "
                else:
                    if a != 7:
                        s+= f'{months[1][i][a]}\n'   
            s += '\n'
            print(s)
            s = ''
        print(spisok)

class Celebrate:
    def __init__(self,dates,ch_religion):
        self.dates = str(dates)
        self.ch_religion = list(ch_religion)    

    def check_day(self): # проверка даты на праздник

        # Резервирование базы данных в переменные  
        file = "celebrates.json"
        file_days = "celebrates_days.json"
        data = pandas.read_json(file)
        data_days = pandas.read_json(file_days)

        # Выборка чисел из !введенной даты
        d_year = int((self.dates).split(".")[2])
        d_month = int((self.dates).split(".")[1])
        d_day = int((self.dates).split(".")[0])
        
        # Для перебора данных из базы данных
        date = f'{int((self.dates).split(".")[1])}.{(self.dates).split(".")[0]}' #Дата формата месяц.день
        days_to_date = dt(d_year,d_month,d_day) - dt(d_year,1,1) # Вычисление дней
        days_to_date = days_to_date.days  #Количество прошедших дней за год
        
        if (d_year % 4 == 0)and((d_day > 27)or(d_month >= 2)): # Проверка на високосность
            days_to_date += 1
        print(days_to_date)
        
        # Перебор данных и сравнивание с датой и днем
        list_of_celebrates = []
        rel = self.ch_religion
        
        # перебор по датам
        for i in range(len(data.index)):
            if date == str(data["dates"][i]):
                for j in range(len(rel)):
                    if rel[j] == str(data["religion"][i]):
                        list_of_celebrates.append(data["named"][i])
        
        # перебор по дням
        for i in range(len(data_days.index)):
            if str(days_to_date) == str(data_days["days"][i]):
                for j in range(len(rel)):
                    if rel[j] == str(data_days["religion"][i]):
                        list_of_celebrates.append(data_days["named"][i])
        
        # перебор по "день на неделе"

        # подготовка входных данных    
        days_of_week = dt.isocalendar(dt(d_year,d_month,d_day))
        print(days_of_week)
        week = int(days_of_week[1])/7
        print(week)
        
        if isinstance(week,float):
            # если с плавающей точкой
            if week < round(week):
                week = round(week) - 1
            else:
                week = round(week)
        elif isinstance(week,int):
            # если число целочисленное 
            week = week
        format_to_db = f'{d_month}/{week}/{days_of_week[2]}'
        # Конец подготовки
        
        for i in range(len(data_days.index)):
            if str(format_to_db) == str(data_days["days"][i]):
                for j in range(len(rel)):
                    if rel[j] == str(data_days["religion"][i]):
                        list_of_celebrates.append(data_days["named"][i])

        return(list_of_celebrates)
    
    def create_string(self,arg):
        add_date = str(arg.split(";")[0])
        add_named =  str(arg.split(";")[1])
        add_religion =  str(arg.split(";")[2])
        add_religion = add_religion.capitalize()
        addit = '\t{'+'"dates":'+f'"{add_date}",'+'"named":'+f'"{add_named}",'+'"religion":'+f'"{add_religion}"'+'}'
        print(addit)
        file = "celebrates.json"

        f = open(file,encoding="utf-8").readlines() 
        for i in [0,-1]: 
            f.pop(i)

        s = f[len(f)-1]
        s = s.split("\n")[0]
        f.remove(f[len(f)-1])
        f.append((s+',\n'))
        f.append(addit)

        with open(file,'w',encoding="utf-8") as F:
            F.writelines("[\n")
            F.writelines(f)
            F.writelines("\n]")
        
        return True



# Ввод числа и развиение на отдельные компоненты
now_d = str(input("Введите дату в формате дд.мм.гггг .\n"))

while (len(now_d) != 10) or (len(now_d.split(".")) != 3) or ((len(now_d.split(".")[2])) != 4):
    print("Неверно введена дата или формат!")
    now_d = str(input("Введите дату в формате дд.мм.гггг .\n"))

year = int(now_d.split(".")[2])

cal = Сalendar(2020,months)
cal.get_calendar()

# Выбор религий
choose_rel = str(input("Введите через запятую и без отступов религии которые вас интересуют(либо оставьте поле пустым).\n Христианство \n Буддизм \n Ислам \n Все \n Нет \n"))

religion_list = ["Христианство","Буддизм","Ислам","Нет"]
religion = choose_rel.split(",")
for i in range(len(religion)):
    if religion[i] == '':
        religion[i] = "Нет"
    if religion[i] == ('Все')or('все'):
        religion == "Христианство,Буддизм,Ислам"
    elif religion[i] not in religion_list:
        print(religion[i],' - не прописаная в словаре религия, поэтому была удалена')
        religion.remove(religion[i])
    else:
        religion[i].capitalize
choose_rel = ''


day = Celebrate(now_d,religion)
cel_day = day.check_day()


# Вывод обработанной даты в сообщение
for i in range(len(religion)):
    if i != len(religion)-1:
        choose_rel += str(religion[i]) + ','
    else:
        choose_rel += str(religion[i])

message = f"\n Сегодня {now_d} \nРелигии {choose_rel} отмечают такие праздники как "

for i in range(len(cel_day)):
    if i != len(cel_day)-1:
        message += str(cel_day[i]) + ','
    else:
        message += str(cel_day[i]) + '.'        

print(message)

# Вопрос о добавлении праздника
choise  = int(input('Желаете добавить собственный праздник ?\n *Выберите цифру варианта ответа* \n 1.Да \n 2.Нет \n'))
if choise == 1:
    adding_to_base = str(input("Введите праздник в форме - <мм.дд;Название;Религия>(Без отступов!)  \n"))
    print(adding_to_base)
    created = day.create_string(adding_to_base)
