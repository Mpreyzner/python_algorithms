

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    smaller = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


print(quick_sort([0,99, -1, 423, 5]))
