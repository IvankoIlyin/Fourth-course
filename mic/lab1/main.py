def input_array():
    try:
        input_str = input("Введіть елементи масиву через пробіл: ")
        input_list = [int(x) for x in input_str.split()]
        return input_list
    except ValueError:
        print("Будь ласка, введіть лише числа, розділені пробілами.")
        return input_array()


def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, swaps



def start_lab1():
    arr=input_array()
    sorted_array, swaps = bubble_sort(arr)
    print("Відсортований масив:", sorted_array)
    print("Кількість перестановок:", swaps)



start_lab1()