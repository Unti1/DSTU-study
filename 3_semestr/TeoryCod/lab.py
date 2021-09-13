import sys

BITMAP_Header = 54


# EncodeFile - имя пути к зашифровоной картинке
def encode(fl, flTo,EncodeFile, position, n):
    binary_str = ''
    
    # открываем вшиваемое изображение для считывания данных о изображении
    
    with open(fl, 'rb') as f:
        
        while True:
            s = f.read(1)
            if not s:
                break

            s = ord(s) # перевод в юникод
            b = bin(s).replace('0b', '') #перевод в биты
            
            while (len(b)) < 8:
                b = "0" + b

            binary_str += b # добавление в битов в строку
    
    cod = len(binary_str)
    # созадем новый файл в который прописываем данные вшиваемого изображения
    with open(EncodeFile, 'wb') as encf:
        # открываем файл в которое будет происходить вшитие
        with open(flTo, 'rb') as ft:
            hd = ft.read(BITMAP_Header)
            encf.write(hd)
            # чтение и превод в биты
            while len(binary_str) != 0:
                
                try:
                    symbol = binary_str[:n]
                    binary_str = binary_str[n:]

                    sft = ft.read(1)
                    sft = ord(sft)
                    bft = bin(sft).replace('0b', '')

                except:
                    break
    
                
                while (len(bft)) < 8:
                    bft = "0" + bft
                
                try:
                    bft = bft[:position] + symbol + bft[position + n:]
                except:
                    bft = bft[:position] + symbol
                
                bft = int(bft, 2)
                
                encf.write((bft.to_bytes(1, sys.byteorder)))
            
            final = ft.read()
            encf.write(final)

    print('Успешное кодирование !')
    return (cod)


def decode(flFrom,flTo,position, n, lenght):

    decoding_str = 0
    strafe = ''
    
    with open(flFrom, 'rb') as f:
        header = f.read(BITMAP_Header)
    
        with open(flTo, 'wb') as ft:
            while ((decoding_str) < lenght):
                
                try:

                    while len(strafe) < 8:
                        sft = f.read(1)
                        sft = ord(sft)
                        bft = bin(sft).replace('0b', '')
                       
                        while (len(bft)) < 8:
                            bft = "0" + bft
                        final_str = bft[position:n + position]
                        strafe += final_str

                    st1 = strafe[:8]
                    strafe = strafe[8:]
                    final = int(st1, 2)
                    final = final.to_bytes(1, sys.byteorder)
                    
                    ft.write(final)
                    decoding_str += 8
                
                except:
                    print('Неудачное декодирование ! Ошибка при прописовании битов')
                    return() 
    print('Успешное декодирование !')

# Задание параметров сдвига по битам
BIT_deep = 4
pos = 3

# Инициация программы
if __name__ == "__main__":
    if BIT_deep + pos <= 8:
        encode_image = encode('temporary_files\\2.bmp', 'temporary_files\\1.bmp',"temporary_files\\encoded.bmp", pos, BIT_deep)
        decode('temporary_files\\encoded.bmp','temporary_files\\decoded.bmp',pos, BIT_deep, encode_image)
    else:
        print('Подобное смещение битов невозможно !')
        