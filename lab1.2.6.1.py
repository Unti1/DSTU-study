import adodbapi
 
database = "db1.mdb"
constr = 'Provider=Microsoft.Jet.OLEDB.4.0; Data Source=%s'
tablename = "address"
 
# Подключаемся к базе данных.
conn = adodbapi.connect(constr)
 
# Создаем курсор.
cur = conn.cursor()
 
# Получаем все данные.
sql = "select * from %s" % tablename
cur.execute(sql)
 
# Показываем результат.
result = cur.fetchall()
for item in result:
    print(item)
 
# Завершаем подключение.
cur.close()
conn.close()

 """Ans = str(input('Хотите добватить пользователя в базу ?(Да/Нет)'))
    if Ans == ('Да')or('да')or('дА')or('ДА'):
        counter = 0
        while counter == 0:
            add_number = (persons[len(persons)-1].number)+1
            #print(add_number)
            add_name = str(input('Введите Ф.И.О. : '))
            add_birth = str(input('Введите дату рождения (формата : dd/mm/yyyy):'))
            add_w_work = int(input('Введите стаж: '))
            add_profession = str(input('Введите профессию: '))
            add_department = str(input('Введите кафедру: '))
            add_w_about = str(input('Введите примечаний: '))
            persons.append(db(add_number,add_name,add_birth,add_w_work,add_profession,add_department,add_w_about))
            Ans2 = str(input('Хотите добватить ещё пользователя в базу ?(Да/Нет)'))
            """-----------------------------------------------------------------"""
            if Ans2 == ('Да')or('да')or('дА')or('ДА'):
                counter == 0
            elif Ans2 == ('Нет')or('нЕТ')or('НЕТ')or('НеТ'):
                counter += 1
            else:
                print('Был введен неверный ответ!')
            """-----------------------------------------------------------------"""
    elif Ans == ('Нет')or('нЕТ')or('НЕТ')or('НеТ'):
        print('Продолжается тело программы')
    else:
        print('Был введен неверный ответ!')"""