translations = {
    "cat": "кіт",
    "dog": "собака",
    "sun": "сонце",
    "moon": "місяць",
    "book": "книга",
    "car": "машина"
}

word = input("Введіть слово англійською: ")

if word in translations:
    print("Переклад:", translations[word])
else:
    print("Слово не знайдено")