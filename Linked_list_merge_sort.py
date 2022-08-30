from Linked_list import Linkedlist


def merge_sort(Linked_list):
    if Linkedlist.size() == 1:
        return Linkedlist

    elif Linked_list.head is None:
        return Linkedlist

    left_half, right_half = split(Linkedlist)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def split(Linked_list):
    if Linkedlist is None or Linkedlist.head is None:
        left_half = Linkedlist
        right_half = None

        return left_half, right_half

    else:
        size = Linked_list.size()
        mid = size // 2

        mid_node = Linked_list.node_at_index(mid - 1)
        left_half = Linked_list
        right_half = Linkedlist()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    merged = Linkedlist()

    merged.add(0)

    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = right_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node
    head = merged.head.next_node
    merged.head = head

    return merged


l = Linkedlist()

l.add(2)
l.add(899)
l.add(98)
l.add(19)
l.add(52)

print(l)

sorted_list = merge_sort(l)

print(sorted)
