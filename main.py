import random
import timeit

# Реалізація сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивний виклик для кожної половини
        merge_sort(left_half)
        merge_sort(right_half)

        # Злиття двох відсортованих половин
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Додавання залишків
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Реалізація сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Переміщення елементів, які більші за key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Функція для генерації тестових масивів
def generate_test_data(size, order='random'):
    if order == 'random':
        return [random.randint(0, 10000) for _ in range(size)]
    elif order == 'sorted':
        return list(range(size))
    elif order == 'reversed':
        return list(range(size, 0, -1))


# Порівняння алгоритмів
def compare_algorithms():
    sizes = [10, 100, 1000, 10000]
    for size in sizes:
        data = generate_test_data(size, order='random')

        # Копії для кожного алгоритму
        data_merge = data[:]
        data_insertion = data[:]
        data_sorted = data[:]
        data_sort = data[:]

        print(f"Number of elements: {size}")

        # Вимірювання часу Merge Sort
        merge_time = timeit.timeit(lambda: merge_sort(data_merge), number=1)
        print(f"Merge Sort: {merge_time:.10f} seconds")

        # Вимірювання часу Insertion Sort
        if size <= 1000:  # Insertion Sort занадто повільний для великих масивів
            insertion_time = timeit.timeit(lambda: insertion_sort(data_insertion), number=1)
            print(f"Insertion Sort: {insertion_time:.10f} seconds")
        else:
            print("Insertion Sort: skipped (too slow)")

        # Вимірювання часу sorted()
        sorted_time = timeit.timeit(lambda: sorted(data_sorted), number=1)
        print(f"Timsort (sorted): {sorted_time:.10f} seconds")

        # Вимірювання часу sort()
        sort_time = timeit.timeit(lambda: data_sort.sort(), number=1)
        print(f"Timsort (sort): {sort_time:.10f} seconds")

        print()


# Запуск порівняння
if __name__ == "__main__":
    compare_algorithms()
