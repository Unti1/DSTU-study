from io import StringIO
from PIL import Image

img = Image.open("temporary_files/imag.jpg")
# img.show()

# img = Image.open("temporary_files/imag1.jpg")
# img = img.convert("L")
# img.show()

# # Для более ранних версий
# # img = Image.open("temporary_files/imag.jpg", "rb")
# # img.show()

# f = open("temporary_files/imag2.gif", "rb")
# img = Image.open(f)
# img.show()
# f.close()

# f = open("temporary_files/imag2.gif", "rb")
# i = f.read()
# f.close()

# Подключаем модуль StringIO:
f = open("temporary_files/imag2.gif", "rb")
# Сохраните изображение в переменной:
i = f.read()
# i = str(i)
# f.close()  # Закрываем файл
# Передаем объект:
# img = Image.open(StringIO(i))
# выводим изображение на экран:
tempBuff = StringIO()
tempBuff.write(str(i))
# need to jump back to the beginning before handing it off to PIL
tempBuff.seek(0)
img = Image.open(tempBuff)
img.show()
