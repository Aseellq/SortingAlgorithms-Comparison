def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val



def partition(array: object, low: object, high: object) -> object:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        return arr

def hybrid_quick_sort(arr, low, high):
    while low < high:
        if high - low + 1 < 17:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)
            if pivot - low < high - pivot:
                hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1

size = int(input("enter size of input : "))
import random
import time

randList1= []
randList2= []
randList3= []

random.seed(time.time())
for i in range(size + 1):
    n = random.randint(1, 1000)
    randList1.append(n)
    randList2.append(n)
    randList3.append(n)


start1 = time.time()
insertion_sort(randList1,0,size)
end1 = time.time()
print('      time taken by insertionsort algorithm  :', (end1-start1)*1000)


start3 = time.time()
quick_sort(randList3,0,size)
end3 = time.time()
print('      time taken by Quicksort algorithm :', (end3-start3)*1000)

start2 = time.time()
hybrid_quick_sort(randList2, 0, size)
end2 = time.time()
print('      time taken by hybridsort algorithm  :', (end2-start2)*1000)
