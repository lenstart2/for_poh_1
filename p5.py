def bubble_sort(arr):
    n = len(arr)
    # Проходим по массиву
    for i in range(n):
        # Последние i элементов уже на месте
        for j in range(0, n - i - 1):
            # Меняем местами, если текущий элемент больше следующего
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Тестируем сортировку
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Исходный список:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", sorted_numbers)