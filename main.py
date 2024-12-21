import random
import timeit
import pandas as pd


# Реалізація сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

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
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Функція для генерації тестових масивів
def generate_test_data(size, order="random"):
    if order == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif order == "sorted":
        return list(range(size))
    elif order == "reversed":
        return list(range(size, 0, -1))


# Порівняння алгоритмів
def compare_algorithms():
    sizes = [10, 100, 1000, 10000]
    results = []

    for size in sizes:
        data = generate_test_data(size, order="random")

        # Копії для кожного алгоритму
        data_merge = data[:]
        data_insertion = data[:]
        data_sorted = data[:]
        data_sort = data[:]

        merge_time = timeit.timeit(lambda: merge_sort(data_merge), number=1)
        insertion_time = (
            timeit.timeit(lambda: insertion_sort(data_insertion), number=1)
            if size <= 1000
            else "skipped"
        )
        sorted_time = timeit.timeit(lambda: sorted(data_sorted), number=1)
        sort_time = timeit.timeit(lambda: data_sort.sort(), number=1)

        results.append(
            {
                "Size": size,
                "Merge Sort (s)": merge_time,
                "Insertion Sort (s)": insertion_time,
                "Timsort (sorted) (s)": sorted_time,
                "Timsort (sort) (s)": sort_time,
            }
        )
    return pd.DataFrame(results)


# Виконання аналізу
results_df = compare_algorithms()

# Збереження результатів у Markdown файл
def save_results_to_md(df, filename="results.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Результати порівняння алгоритмів сортування\n\n")
        f.write(df.to_markdown(index=False))
        f.write("\n")

# Збереження результатів
save_results_to_md(results_df)
print("Результати збережено у файл 'results.md'")

