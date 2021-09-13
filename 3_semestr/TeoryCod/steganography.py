# -*- coding: utf-8 -*-

from PIL import Image


class Steganography(object):

    @staticmethod
    def __int_to_bin(rgb):
        """Преобразование целочисленного кортежа в двоичный (строковый) кортеж.

         : param rgb: Целочисленный кортеж (например, (220, 110, 96))
         : return: строковый кортеж (например, ("00101010", "11101011", "00010110"))
        """
        r, g, b = rgb
        return ('{0:08b}'.format(r),
                '{0:08b}'.format(g),
                '{0:08b}'.format(b))

    @staticmethod
    def __bin_to_int(rgb):
        """Преобразование двоичный (строковый) кортеж в целочисленный кортеж.

         : param rgb: строковый кортеж (например, ("00101010", "11101011", "00010110"))
         : return: возвращает кортеж int (например, (220, 110, 96))
        """
        r, g, b = rgb
        return (int(r, 2),
                int(g, 2),
                int(b, 2))

    @staticmethod
    def __merge_rgb(rgb1, rgb2):
        """Объедините два кортежа RGB.
         : param rgb1: строковый кортеж (например, ("00101010", "11101011", "00010110"))
         : param rgb2: Другой строковый кортеж
         (например, ("00101010", "11101011", "00010110"))
         : return: Целочисленный кортеж с двумя объединенными значениями RGB.
        """
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        rgb = (r1[:4] + r2[:4],
               g1[:4] + g2[:4],
               b1[:4] + b2[:4])
        return rgb

    @staticmethod
    def merge(img1, img2):
        """Объедините два изображения. Второй будет объединен с первым.

         : param img1: Первое изображение
         : param img2: Второе изображение
         : return: Новое объединенное изображение.
        """

        # Проверьте размеры изображений
        if img2.size[0] > img1.size[0] or img2.size[1] > img1.size[1]:
            raise ValueError('Image 2 should not be larger than Image 1!')

        # Получите пиксельную карту двух изображений
        pixel_map1 = img1.load()
        pixel_map2 = img2.load()

        # Создайте новое изображение, которое будет выводиться
        new_image = Image.new(img1.mode, img1.size)
        pixels_new = new_image.load()

        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                rgb1 = Steganography.__int_to_bin(pixel_map1[i, j])

                # По умолчанию использовать черный пиксель
                rgb2 = Steganography.__int_to_bin((0, 0, 0))

                # Убедитесь, что позиция пиксельной карты действительна для второго изображения
                if i < img2.size[0] and j < img2.size[1]:
                    rgb2 = Steganography.__int_to_bin(pixel_map2[i, j])

                # Объедините два пикселя и преобразуйте их в целочисленный кортеж
                rgb = Steganography.__merge_rgb(rgb1, rgb2)

                pixels_new[i, j] = Steganography.__bin_to_int(rgb)

        return new_image

    @staticmethod
    def unmerge(img):
        """Разъединить изображение.

         : param img: Входное изображение.
         : return: Не объединенное / извлеченное изображение.
        """

        # Загрузите пиксельную карту
        pixel_map = img.load()

        # Создайте новое изображение и загрузите карту пикселей.
        new_image = Image.new(img.mode, img.size)
        pixels_new = new_image.load()

        # Кортеж, используемый для хранения исходного размера изображения
        original_size = img.size

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                # Получить RGB (в виде строкового кортежа) из текущего пикселя
                r, g, b = Steganography.__int_to_bin(pixel_map[i, j])

                # Извлеките последние 4 бита (соответствующие скрытому изображению)
                # Объедините 4 нулевых бита, потому что мы работаем с 8-битными
                rgb = (r[4:] + '0000',
                       g[4:] + '0000',
                       b[4:] + '0000')

                # Преобразуйте его в целочисленный кортеж
                pixels_new[i, j] = Steganography.__bin_to_int(rgb)

                # Если это «действительная» позиция, сохраните ее.
                # как последняя действительная позиция
                if pixels_new[i, j] != (0, 0, 0):
                    original_size = (i + 1, j + 1)

        # Обрезать изображение н а основе "допустимых" пикселей
        new_image = new_image.crop((0, 0, original_size[0], original_size[1]))

        return new_image


def merge(img1, img2, output):
    merged_image = Steganography.merge(Image.open(img1), Image.open(img2))
    merged_image.save(output)

def unmerge(img, output):
    unmerged_image = Steganography.unmerge(Image.open(img))
    unmerged_image.save(output)


# слияние

img1 = 'temporary_files/pic.jpg'
img2 = 'temporary_files/pict.jpg'
out_pic = 'temporary_files/steg_pic.jpg'

merge(img1,img2,out_pic)

# разложение
out_resteg_pic = 'temporary_files/resteg_pic.jpg'
unmerge(out_pic,out_resteg_pic) 