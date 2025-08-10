def count_words(text):
    # Разбиваем текст на слова и убираем знаки препинания
    words = text.lower().split()
    word_count = {}
    # Подсчитываем частоту каждого слова
    for word in words:
        word = word.strip('.,!?')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Тестируем
text = "Кот кот и собака. Собака и кот играют вместе."
result = count_words(text)
for word, count in result.items():
    print(f"Слово '{word}': {count} раз")