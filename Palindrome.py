# O(N) runtime: depends on the length of the string as it is being reversed.

def is_palindrome(s):
    original_string = s
    reversed_string = reverse(s)

    if original_string == reversed_string:
        return True
    return False


def reverse(data):
    # convert string into a list of characters
    data = list(data)
    # points to the first index
    start_index = 0
    # Points to the last index
    end_index = len(data) - 1

    while end_index > start_index:
        # keep swapping items
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    # transform the letters into a string
    return ''.join(data)


def palindrome_python(s):
    if s == s[::-1]:
        return  True
    return False


if __name__ == '__main__':
    print(is_palindrome("madam"))
