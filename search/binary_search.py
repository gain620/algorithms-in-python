def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2  # // is integer divide

        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def recursiveBinarySearch(list, item):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == item:
            return True
        else:
            if item < list[mid]:
                return recursiveBinarySearch(list[:mid], item)
            else:
                return recursiveBinarySearch(list[mid + 1:], item)


testlist = [0, 1, 3, 5, 6, 7, 13, 23, 45, 67]
print(binarySearch(testlist, 43))
print(binarySearch(testlist, 23))
print(recursiveBinarySearch(testlist, 43))
print(recursiveBinarySearch(testlist, 23))
