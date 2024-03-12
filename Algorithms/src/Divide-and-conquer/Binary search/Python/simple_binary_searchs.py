# ======================= < SIMPLE BINARY SEARCH, IMITATING PYTHON BISEC MODULE > ======================= #

def identity(element):
    """Identity function serving as a default key provider."""
    return element


def find_index(elements, value, key=identity):
    """Return the index of value in elements or None."""

    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1

    return None


def find_leftmost_index(elements, value, key=identity):

    index = find_index(elements, value, key)
    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        index += 1
    return index


def find_rightmost_index(elements, value, key=identity):

    index = find_index(elements, value, key)

    if index is not None:
        while index < len(elements) and key(elements[index]) == value:
            index += 1
        index -= 1
    return index


def find_all_indices(elements, value, key=identity):
    """Return a set of indices of elements with matching key."""

    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)

    if left and right:
        return set(range(left, right + 1))
    else:
        return set()


def _get(elements, index):
    """Return element at the given index or None."""
    return None if index is None else elements[index]


def find(elements, value, key=identity):
    """Return an element with matching key or None."""
    return _get(elements, find_index(elements, value, key))


def find_leftmost(elements, value, key=identity):
    """Return the leftmost element or None."""
    return _get(elements, find_leftmost_index(elements, value, key))


def find_rightmost(elements, value, key=identity):
    """Return the rightmost element or None."""
    return _get(elements, find_rightmost_index(elements, value, key))

def find_all(elements, value, key=identity):
    """Return a set of elements with matching key."""
    return {elements[i] for i in find_all_indices(elements, value, key)}


def is_in(elements, value, key=identity):
    """Return True if value is present in elements."""
    return find_index(elements, value, key) is not None


def contains(elements, value, left, right):
    if left <= right:
        middle = (left + right) // 2
        print(middle)
        if elements[middle] == value:
            return True

        elif elements[middle] < value:
            return contains(elements, value, middle + 1, right)
        elif elements[middle] > value:
            return contains(elements, value, left, middle - 1)

    return False


sorted_fruits = ['apple', 'banana', 'orange', 'plum', 'thing',
                 'thing ', 'other', 'thing', 'thing ', 'other']

print(contains(sorted_fruits, 'apple', 0, len(sorted_fruits) - 1))

