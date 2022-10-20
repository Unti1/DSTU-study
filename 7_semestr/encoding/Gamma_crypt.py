import string
alphabeth = *string.ascii_lowercase, * \
    string.ascii_uppercase, *string.digits, *string.whitespace, * \
    tuple("эйцукеёнгшщзхъфывапролджячсмитьбю"), * \
    tuple("эйцукеёнгшщзхъфывапролджячсмитьбю".upper()), *string.punctuation
alphabeth = list(alphabeth)


def encrypt(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)

    # Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])
    # print(keyText)
    # Шифрование
    code = []
    for i in range(textLen):
        code.append(
            alphabeth[(alphabeth.index(text[i]) + alphabeth.index(keyText[i])) % len(alphabeth)])

    return code


def decrypt(code, gamma):
    codeLen = len(code)
    gammaLen = len(gamma)

    # Формируем ключевое слово(растягиваем гамму на длину текста)
    keyText = []
    for i in range(codeLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(codeLen % gammaLen):
        keyText.append(gamma[i])

    # Расшифровка
    text = []
    for i in range(codeLen):
        text.append(
            alphabeth[(alphabeth.index(code[i]) - alphabeth.index(keyText[i]) + len(alphabeth)) % len(alphabeth)])

    return text


if __name__ == "__main__":
    text_code = encrypt(
        "Какой то небольшой текст для кодировки", "21457526138638215")
    print("".join(text_code))
    decrypt_text = decrypt(text_code, "21457526138638215")
    print("".join(decrypt_text))
