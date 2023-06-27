import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(arr, sort_name, iterations=5):
    print(f"\n{sort_name} - 5 Iterasi Pertama:")
    for i in range(iterations):
        print(arr[i], end=" ")
    print("\n")

    print(f"{sort_name} - 5 Iterasi Terakhir:")
    for i in range(len(arr)-iterations, len(arr)):
        print(arr[i], end=" ")
    print("\n")

def print_time(arr, sort_name, execution_time):
    print(f"{sort_name} - Waktu Komputasi: {execution_time:.6f} detik\n")

def print_before_after(arr, sort_name):
    print(f"Sebelum {sort_name}:")
    print(arr)
    print("\nSetelah {sort_name}:")
    sorted_arr, _ = sort_func(arr)
    print(sorted_arr)
    print("\n")

def analyze_algorithm():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    while True:
        print("Pilihan pengurutan:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("0. Keluar")
        choice = int(input("Masukkan pilihan: "))

        if choice == 0:
            break
        elif choice == 1:
            sort_func = bubble_sort
            sort_name = "Bubble Sort"
        elif choice == 2:
            sort_func = insertion_sort
            sort_name = "Insertion Sort"
        else:
            print("Pilihan tidak valid!")
            continue

        print_before_after(arr, sort_name)

        sorted_arr, execution_time = sort_func(arr)

        print_iterations(sorted_arr, sort_name)
        print_time(sorted_arr, sort_name, execution_time)

analyze_algorithm()