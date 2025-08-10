import random

# Компьютер загадывает число
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Угадайте число от 1 до 100!")
while attempts < max_attempts:
    guess = int(input("Введите число: "))
    attempts += 1
    if guess == secret_number:
        print(f"Поздравляем! Вы угадали число за {attempts} попыток!")
        break
    elif guess < secret_number:
        print("Слишком мало!")
    else:
        print("Слишком много!")
if attempts == max_attempts:
    print(f"Игра окончена! Число было {secret_number}.")