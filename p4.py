def is_prime(n):
    # Числа меньше 2 не являются простыми
    if n < 2:
        return False
    # Проверяем делители до корня из n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Находим простые числа в диапазоне
start = 1
end = 50
primes = [num for num in range(start, end + 1) if is_prime(num)]
print(f"Простые числа от {start} до {end}: {primes}")
print(f"Количество простых чисел: {len(primes)}")