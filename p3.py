def is_palindrome(text):
    # Приводим к нижнему регистру и убираем пробелы/знаки
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Проверяем, является ли строка палиндромом
    return cleaned_text == cleaned_text[::-1]

# Тестируем несколько строк
test_strings = ["А роза упала на лапу Азора", "Python", "радар", "hello"]
for s in test_strings:
    if is_palindrome(s):
        print(f"'{s}' — это палиндром!")
    else:
        print(f"'{s}' — не палиндром.")