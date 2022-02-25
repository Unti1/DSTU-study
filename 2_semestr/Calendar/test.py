week = 39/7
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

print(week)