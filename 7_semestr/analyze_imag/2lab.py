from tkinter import Image
from PIL import Image
based_path = "temporary_files/"

img = Image.open(based_path+"pict.jpg")
print(img.mode)
img.show()

obj = img.load()
print(obj[1, 1])  # Получаем цвет пикселя

# Задаем цвет пикселя
obj[1, 1] = (255, 255, 255)
print(obj[1, 1])  # Получаем цвет пикселя
img.show()


print(img.getpixel((1, 1)))
# Изменяем цвет пикселя
img.putpixel((1, 1), (0, 0, 255))
# Получаем цвет пикселя
img.getpixel((1, 1))
img.show()  # Просматриваем изображение


R, G, B = img.split()
mask = Image.new("L", img.size, 128)
img2 = Image.merge("RGBA", (R, G, B, mask))
img2.mode
img2.show()

img = Image.open(based_path+"pict.jpg")
print(img.mode)

img2 = img.convert("RGBA")
print(img2.mode)
img2.show()

img2.convert("P",None,Image.FLOYDSTEINBERG, Image.ADAPTIVE,128)
print(img2.mode)


# Сохранение изображения в текущую папку в формате JPEG:
img.save("testout/tmp.jpg")
# в формате BMP:
img.save("testout/tmp.bmp", "BMP")
f = open("testout/tmp2.bmp", "wb")
# Передаем файловый объект
img.save(f, "BMP")
f.close()

# 1. Создайте черный квадрат.
img = Image.new("RGB", (100, 100))
img.show() # Черный квадрат
# 2. Создайте красный квадрат.
img = Image.new("RGB", (100, 100), (255, 0, 0))
img.show() # Красный квадрат
# 3. Создайте Зеленый квадрат.
img = Image.new("RGB", (100, 100), "green")
img.show() # Зеленый квадрат
# 4. Создайте красный квадрат.
img = Image.new("RGB", (100, 100), "#f00")
img.show() # тоже красный квадрат
# 5. Создайте белый квадрат.
img = Image.new("RGB", (100, 100), "white")
img.show() # Белый квадрат
# 6. Создайте серый квадрат.
img = Image.new("RGB", (320, 240), "silver")
img.show() # Серый квадрат
# 7. Создайте цветной прямоугольник.
img = Image.new("RGB", (320, 240), "rgb(205,100,200)")
img.show() # цветной прямоугольник
# 8. Создайте цветной прямоугольник (Каналы в процентах).
img = Image.new("RGB", (320, 240), "rgb(10%,100%,40%)")
img.show() # цветной прямоугольник. Каналы в процентах
# 9. Создайте цветной прямоугольник заданного цвета. Затем пом еняйте этот
img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show() # сиреневый прямоугольник
for x in range(640):
    for y in range(480):
        img.putpixel((x,y),(0,160,0))

img.save("testout/okno.png", "PNG")
img.show() # зеленый прямоугольник

# 10. Создайте прямоугольник заданного цвета (функциональная раскраска).
img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show() # сиреневый прямоугольник
for x in range(640):
    for y in range(480):
        img.putpixel((x,y),(int(x/3),int((x+y)/6),int(y/3)))
img.save("okno.png", "PNG")
img.show() # прямоугольник с функциональной раскраской