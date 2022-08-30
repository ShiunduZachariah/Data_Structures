def binary_search(listA, target):
    first = 0
    last = len(listA) - 1

    while first <= last:
        midpoint = (first + last)//2

        if listA[midpoint] == target:
            return midpoint

        elif listA[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target Not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
