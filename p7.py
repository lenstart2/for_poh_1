def fibonacci(n):
    # Первые два числа Фибоначчи
    fib_sequence = [0, 1]
    # Генерируем следующие числа
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Генерируем первые 10 чисел Фибоначчи
n = 10
fib_numbers = fibonacci(n)
print(f"Первые {n} чисел Фибоначчи: {fib_numbers}")