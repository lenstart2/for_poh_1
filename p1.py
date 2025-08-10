import random
import string


def generate_password(length=12):
    # Определяем набор символов
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    # Генерируем пароль
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# Генерируем 5 паролей
for i in range(5):
    pwd = generate_password()
    print(f"Пароль {i + 1}: {pwd}")