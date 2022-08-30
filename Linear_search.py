def linear_search(list, target):
    """

    :param list: Checks the list
    :param target: Value we are looking for
    :return: target index or None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target Not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
