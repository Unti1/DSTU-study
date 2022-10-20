
from random import shuffle


def encode_single_reshuffle(origin_key, origin_text):
    # слияние и снижение регистра
    clear_text = ''.join(origin_text.split(' ')).lower()
    # соотношение числа букв в шифруемом слове и с ключом
    k = len(clear_text) // len(origin_key)
    shuffled = {}  # словарь для нумерации
    """
    Генерация словаря по буквам ключа
    """
    for index, ch in enumerate(origin_key.lower()):
        if ch in shuffled:
            shuffled[ch] += clear_text[index * k: index * k + k]
        else:
            shuffled[ch] = clear_text[index * k: index * k + k]
    print(shuffled)
    # print([''.join([shuffled[key][index] for key in sorted(shuffled.keys())]) for index in range(k)])
    shuffled_text = ''.join([''.join([shuffled[key][index]
                                      for key in sorted(shuffled.keys())]) for index in range(k)])
    # print(shuffled_text)
    return ''.join([shuffled_text[index: index + k] for index in range(0, len(shuffled_text), k)]).upper()


def decode_single_reshuffle(origin_key, reshuffled_text):
    # определение количества строк [1 этап]
    rows = len(reshuffled_text) // len(origin_key)
    # проверка на четность относительно текста и ключа [2 этап]
    if len(reshuffled_text) % len(origin_key) != 0:
        rows += 1

    # [1 этап] Задаем индексацию по где какая буква стоит в ключе
    indexes = sorted([(index, value) for index, value in enumerate(
        origin_key)], key=lambda item: item[1])
    # print(indexes)
    # [2 этап] Теперь индексируем места где будут стоять буквы после сортировки по алфовиту
    indexes = sorted([(index, value) for index, value in enumerate(
        indexes)], key=lambda item: item[1][0])
    # print(indexes)
    result = ''

    for index in indexes:  # проход по индексированию
        for row in range(rows):  # по количеству строк
            # задаем позицию из нумерации(сортированной) + длины слова помноженую на текужую строку
            position = index[0] + len(origin_key) * row
            if position < len(reshuffled_text):
                result += reshuffled_text[position]
    return (result)


def code_doc(origin_key: str, func):
    with open(f"7_semestr/encoding/input.txt", "r", encoding="utf-8") as fl:
        text = "".join(fl.readlines())

    shuffled = func(origin_key, text)
    with open("7_semestr/encoding/output.txt", "w", encoding="utf-8") as fl:
        fl.write(shuffled)


if __name__ == "__main__":
    # тестирование на простых строках
    # key = 'eXhibitiON'
    # text = 'ТЕРМИНАТОР ПРИБЫВАЕТ СЕДЬМОГО В ПОЛНОЧЬ'
    # enc = encode_single_reshuffle(key, text)
    # dec = decode_single_reshuffle(key, enc)

    # code_doc(key, encode_single_reshuffle)
    # code_doc(key, decode_single_reshuffle)
    pass
