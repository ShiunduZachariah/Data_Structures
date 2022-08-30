def merge_sort(list):
    """
    Sorts the list in ascending order
    :return new sorted list
    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursivley sort the sublists
    Combine: Merge sort the sublists
    :param list:
    :return:
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list into sublists
    Returns two sublists - left and right
    :param list:
    :return:
    """
    mid = len(list) // 2
    left = list[: mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    merge two lists(arrays)
    sorts them in the process
    :returns merged lists
    :param left:
    :param right:
    :return:
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1

        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)

print(l)
print(verify_sorted(alist))
print(verify_sorted(l))
