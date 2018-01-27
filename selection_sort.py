def find_smallest(array):
    # selection search
    smallest = array[0]
    index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            index = i
    return index


def selection_sort(array):
    sorted = []

    for i in range(len(array)):
        smallest = find_smallest(array)
        sorted.append(array.pop(smallest))
    return sorted


sorted = selection_sort([-11, 0, 22, -5, 1, 255, 42, -666])
print(sorted)
