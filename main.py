import random
def genArr(len_arr):
    arr = []
    for i in range(len_arr):
        arr.append(random.randint(1, 1000))
    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = genArr(20) #задаем кол-во значений в списке
heapSort(arr)
n = len(arr)
step = ''
for i in range(n):
    print(f'|{step} {arr[i]}')
    step += ' '