class db:
    def __init__(self,number,name,birth_date,w_age,profession,department,w_about):
        self.number = number
        self.name = name
        self.birth_date = birth_date
        self.w_age = w_age
        self.profession = profession
        self.department = department
        self.w_about = w_about

    def show_list(self):
        return(f'Номер : {self.number}| ФИО: {self.name} | Дата рождения : {self.birth_date} | Стаж работы : {self.w_age} | Профессия : {self.profession} | Кафедра : {self.department} | Примечания: {self.w_about}')
    
    def find_w_age(self):
        if self.w_age > 20:
            return(f'Номер : {self.number}| ФИО: {self.name} | Дата рождения : {self.birth_date} | Стаж работы : {self.w_age} | Профессия : {self.profession} | Кафедра : {self.department} | Примечания: {self.w_about}') 

    def find_professon(self):
        if self.profession == find_prof:
            return(f'Номер : {self.number}| ФИО: {self.name} | Дата рождения : {self.birth_date} | Стаж работы : {self.w_age} | Профессия : {self.profession} | Кафедра : {self.department} | Примечания: {self.w_about}') 

    def add_person(self):
            """add_number = (persons[len(persons)-1].number)+1
            add_name = str(input('Введите Ф.И.О. : '))
            add_birth = str(input('Введите дату рождения (формата : dd/mm/yyyy):'))
            add_w_work = int(input('Введите стаж: '))
            add_profession = str(input('Введите профессию: '))
            add_department = str(input('Введите кафедру: '))
            add_w_about = str(input('Введите примечаний: '))"""
            return(persons.append(db(
                (persons[len(persons)-1].number)+1,
                str(input('Введите Ф.И.О. : ')),
                str(input('Введите дату рождения (формата : dd/mm/yyyy):')),
                int(input('Введите стаж: ')),
                str(input('Введите профессию: ')),
                str(input('Введите кафедру: ')),
                str(input('Введите примечаний: ')))))


# Уже заданная база
persons =  [
    (db('Номерной индекс','ФИО','Дата рождения','Стаж работы','Должность','Кафедра','Примечания')),
    (db(1,'Скляренко Павел Викторович','12/12/1976',23,'Доцент','ИИВТ','Примечаний нет')),
    (db(2,'Кострама Игорь Павлович','12/12/1976',23,'Доцент','ИИВТ','Примечаний нет')),
    (db(3,'Сидорчук Иван Васильевич','25/05/1992',10,'Профессор','ИИВТ','Примечаний нет')),
    (db(4,'Сидорович Андрей Иванович','15/02/1994',5,'Доцент','ИИВТ','Примечаний нет')),
    (db(5,'Прокофьев Евгений Викторович','03/09/1970',24,'Профессор','ИИВТ','Примечаний нет')),
    (db(6,'Радченко Валерий Петрович','06/04/1974',20,'Декан','ИИВТ','Примечаний нет')),
    (db(7,'Иванов Павел Викторович','14/02/1986',14,'Консультант','ИИВТ','Примечаний нет'))
]

# Вывод списка
print('Вывод базы данных')
for i in range(1,len(persons)):
    print(persons[i].show_list())

print('_'*150,'\n')

# Добавление нового пользователя
try:
    ChooseAns = int(input('Выберите комманду действие: \n 1.Добавить \n'))
except:
    print('[Error] Неверно введенный формат в поле ввода\n Программа продолжает работу...')
if ChooseAns == 1:
    persons[len(persons)-1].add_person()

print('_'*150,'\n')

print('Повторный вывод баззы данных')
for i in range(1,len(persons)):
    print(persons[i].show_list())

print('_'*150,'\n')

# Вывод поиска по стажу (фиксированный)
print('Вывод поиска , стаж > 20')
for i in range(1,len(persons)):
    if (persons[i].find_w_age()) != None:
        print(persons[i].find_w_age())

print('_'*150,'\n')

# Поиск по профессии (динамический)

find_prof = str(input('Введите профессию которую нужно найти (оставьте поле пустым если поиск не нужен) :'))
if find_prof != '':
    for i in range(1,len(persons)):
        if (persons[i].find_professon()) != None:
            print(persons[i].find_professon())
else:
    print('Поиск не произведен')