import string
import json
import os
import tools
import time
import Gamma_crypt


def is_prime(n, m):
    """Проверка на взаимопростые числа"""
    if m == 0:
        return n
    else:
        return is_prime(m, n % m)


def two_primes(n, m):
    return is_prime(n, m) == 1


def self_random_method(n: int, max_len: int) -> list:
    """
    Args:
        n (int): Количество случайных значений
        max_len(int): Максимальная длина числа
    Returns:
        list: Список случайных значений
    """
    try:
        based_num = str(round(time.time() * 10**(10*n)))
        lst = []
        count = -1
        last_limit = -n
        for _ in range(n):
            match based_num[count]:
                case 0:
                    limit = 1
                case range(1, max_len):
                    limit = int(based_num[count])
                case _:
                    limit = int(based_num[count])
            count -= 1
            num = int(based_num[last_limit-limit:last_limit])
            last_limit -= limit
            lst.append(num)
        return lst
    except ValueError:
        return (self_random_method(n, max_len))


def generate_current_values():
    tools.set_key(tools.dotenv_path, "n", "24")
    n = int(os.getenv('n'))
    m = 2**n
    tools.set_key(tools.dotenv_path, "m", str(m))
    a, b, c0 = self_random_method(3, n)

    while two_primes(b, m) == False and b % 2 == 0:
        b = self_random_method(1, n)[0]
    while a % 4 != 1:
        a = self_random_method(1, n)[0]
    if a < m and b < m and c0 < m:
        tools.set_key(tools.dotenv_path, "a", str(a))
        tools.set_key(tools.dotenv_path, "b", str(b))
        tools.set_key(tools.dotenv_path, "c0", str(c0))
        return a, b, c0
    else:
        return (generate_current_values())


def random_generation(num):
    a = int(os.getenv("a"))
    b = int(os.getenv("b"))
    c0 = int(os.getenv("c0"))
    c = []
    n = int(os.getenv("n"))
    m = 2**n
    for i in range(num-1):
        match i:
            case 0:
                c.append((a*c0 + b) % m)
            case _:
                c.append((a*c[i-1] + b) % m)
    tools.set_key(tools.dotenv_path, 'c', str(c))


def create_key_file():
    c = json.loads(os.getenv("c"))
    print(c)
    with open("temporary_files/input.txt", "r") as fl:
        text = fl.read()
        lenght_key = len(text)

    with open("temporary_files/token.key", "w") as fl:
        try:
            random_generation(lenght_key)
            text = ""
            i = 0
            while len(text) < lenght_key:
                text += str(c[i])
                i += 1

            text = text[:lenght_key]
            fl.write(text)
        except:
            generate_current_values()
            create_key_file()


def encripting_file(f_name):
    with open("temporary_files/input.txt", "r", encoding="utf-8") as fl:
        text = fl.read()

    with open(f"temporary_files/token.key", "r", encoding="utf-8") as fl_key:
        gamma = fl_key.read()
    with open(f"testout/{f_name}.txt", "w", encoding="utf-8") as fl:
        fl.write("".join(Gamma_crypt.encrypt(text, gamma)))


def decripting_file(f_name):
    with open(f"testout/{f_name}.txt", "r", encoding="utf-8") as fl:
        code = fl.read()

    with open(f"temporary_files/token.key", "r", encoding="utf-8") as fl_key:
        gamma = fl_key.read()

    with open(f"testout/{f_name}_decrypted.txt", "w", encoding="utf-8") as fl:
        fl.write("".join(Gamma_crypt.decrypt(code, gamma)))


def random_gist():
    m = int(os.getenv("m"))
    n = int(os.getenv("n"))
    c = json.loads(os.getenv("c"))
    print(c)
    import matplotlib.pyplot as plt
    counter = 100
    x = 0
    intervals = []
    inter_dct = {}
    for _ in range(counter):
        x += m//counter
        intervals.append(x)
        inter_dct[range(x-m//counter, x)] = 0
    for ranges in inter_dct.keys():
        for val in c:
            if val in ranges:
                inter_dct[ranges] += 1
    counts_inter_dct = inter_dct.values()

    # Относительные частоты
    for ranges in inter_dct:
        inter_dct[ranges] = inter_dct[ranges]/counter
    freq = sum(inter_dct.values())/counter
    c.sort()
    plt.bar(counts_inter_dct, counts_inter_dct, intervals)
    plt.title(f"Общая частота повторений: {round(freq*100,4)}%")
    plt.ylabel('Количество повторений')
    plt.xlabel('Промежутки')
    # plt.figure(figsize=(16, 9))
    plt.show()


def GUI():
    while True:
        print("Выберите из пунктов:\n1.Сгенерировать новые параметры ГСПЧ.\n2.На основании текущих параметров, сгенерировать ГСПЧ.\n3. Вывести гистограмму частоты значений ГСПЧ\n4. Задать ключевой файл.\n5. Зашифровать файл.\n6. Расшифровать файл по текущему ключу")
        inp = input("\n>>> ")
        match inp:
            case "1":
                generate_current_values()
                a = os.getenv("a")
                b = os.getenv("b")
                c0 = os.getenv("c0")
                print(f"Текущие значения:\n\ta: {a}\n\tb: {b}\n\tc0: {c0}")
            case "2":
                num = int(input("\nВведите количество случайных чисел"))
                print(random_generation(num))
            case "3":
                random_gist()
            case "4":
                create_key_file()
                print("Ключевой файл создан")
            case "5":
                print("Введите название для зашифровонного файла.")
                name = input("\n>>>")
                encripting_file(name)
                print("Файл закодирован")
            case "6":
                print(
                    "Введите название зашифрованного файла который нужно расшифровать.")
                name = input("\n>>>")
                decripting_file(name)
                print(f"Декодирован в {name}_decrypted.txt")
            case _:
                print("Такого варианта ответа нету")
        print("--"*50)


if __name__ == "__main__":
    GUI()
